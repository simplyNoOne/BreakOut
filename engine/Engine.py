import pygame
from engine.Scene import Scene
from engine.ResourceManager import ResourceManager
from engine.components.TextureComponent import TextureComponent
from engine.components.CollisionComponent import CollisionComponent
from engine.components.SoundComponent import SoundComponent
from engine.enums import CollisionResponse, Mobility

class Engine:

    _instance = None

    @staticmethod
    def get():
        if Engine._instance is None:
            Engine._instance = Engine()
        return Engine._instance
    

    def __init__(self):
        self._window : pygame.Surface = None
        self._active_scene : Scene = None
        self._events : list[pygame.event.Event] = []
        self._static_colliders : list[CollisionComponent] = []
        self._dynamic_colliders : list[CollisionComponent] = []
        self._static_future_colliders : list[CollisionComponent] = []
        self._dynamic_future_colliders : list[CollisionComponent] = []
        self._clock = pygame.time.Clock()
        self._fps = 180
        self._width = 1300
        self._height = 700
        self._scene_changing = False
        self._frame_time = (1 / self._fps)
        self._running = False
        self._paused = False
        self._wait_time = 0
        self._delayed_functions = []

 
    def load(self):
        pygame.init()
        self._window = pygame.display.set_mode((self._width, self._height))
        self._clock = pygame.time.Clock()
        ResourceManager.get().load_resources()
        ResourceManager.get().register_component("TextureComponent", TextureComponent())
        ResourceManager.get().register_component("CollisionComponent", CollisionComponent())
        ResourceManager.get().register_component("SoundComponent", SoundComponent())
        self._running = True
        
    def register_for_collision(self, collider : CollisionComponent):
        if collider.get_mobility() == Mobility.DYNAMIC:
            self._dynamic_future_colliders.append(collider)
        else:
            self._static_future_colliders.append(collider)

    def unregister_for_collision(self, collider : CollisionComponent):
        if collider.get_mobility() == Mobility.DYNAMIC:
            self._dynamic_future_colliders.remove(collider)
        else:
            self._static_future_colliders.remove(collider)
        

    def get_events(self) -> list[pygame.event.Event]:
        return self._events

    def set_active_scene(self, scene_name : str):
        scene = ResourceManager.get().get_scene(scene_name)
        if self._active_scene is not None:
            self._scene_changing = True
            self._active_scene.unload()
        self._active_scene = scene
        self._active_scene.load()
        self.draw()
        pygame.time.delay(200)
        self._scene_changing = False

    def get_active_scene(self) -> Scene:
        return self._active_scene
    
    def play_music(self, track_name, volume_percent):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        pygame.mixer.music.load(ResourceManager.get().get_music(track_name))
        pygame.mixer.music.set_volume(volume_percent / 100)
        pygame.mixer.music.play(-1)

    def resume(self):
        self._paused = False

    def pause(self):
        self._paused = True

    def wait(self, time):
        self._paused = True
        self.set_function_delay(self.resume, time)

    def set_function_delay(self, func, time):
        self._delayed_functions.append([func, time])

    def main_loop(self):        
        while self._running:
            self._clock.tick(self._fps)
            for func in self._delayed_functions:
                if func[1] > 0:
                    func[1] -= self._frame_time
                else:
                    func[0]()
                    self._delayed_functions.remove(func)
            self._events.clear()
            if self._paused:
                continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                else:
                    self._events.append(event)
            if not self._scene_changing:
                self._active_scene.update(self._frame_time)
                self.check_collisions()
                self.draw()

    def check_collisions(self):
        self._static_colliders = self._static_future_colliders.copy()
        self._dynamic_colliders = self._dynamic_future_colliders.copy()
        if len(self._dynamic_colliders) > 0:
            for i in range(len(self._dynamic_colliders)):
                if self._dynamic_colliders[i].get_response() == CollisionResponse.IGNORE:
                    continue
                for j in range(i + 1, len(self._dynamic_colliders)):
                    self.collide_two(self._dynamic_colliders[i], self._dynamic_colliders[j])
                for j in range(len(self._static_colliders)):
                    self.collide_two(self._dynamic_colliders[i], self._static_colliders[j])
                self._dynamic_colliders[i].update_collisions()
            for i in range(len(self._static_colliders)):
                self._static_colliders[i].update_collisions()

    def collide_two(self, collider : CollisionComponent, other : CollisionComponent):
        if other.get_response() == CollisionResponse.IGNORE:
            return
        collision_already_checked = False
        intersects = False
        if collider.can_collide_with(other):
            collision_already_checked = True
            intersects= self.check_intersects(collider.get_collision_bounds(), other.get_collision_bounds())
            if intersects:
                collider.on_collision(other)
        if other.can_collide_with(collider):
            if not collision_already_checked:
                intersects = self.check_intersects(collider.get_collision_bounds(), other.get_collision_bounds())
            if intersects:
                other.on_collision(collider)

    def quit_game(self):
        self._running = False

    def unload(self):
        self._active_scene.unload()
        pygame.quit()

    def draw(self):
        self._window.fill((0, 0, 0)) 
        self._active_scene.draw(self._window)
        pygame.display.flip()

    def get_window_size(self) -> tuple[int, int]:
        return self._width, self._height

    def check_intersects(self, rect1 : pygame.Rect, rect2 : pygame.Rect):
        return rect1.colliderect(rect2)
