import pygame
from engine.Scene import Scene
from engine.ResourceManager import ResourceManager
from engine.components.TextureComponent import TextureComponent
from engine.components.CollisionComponent import CollisionComponent
from engine.enums import CollisionResponse

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
        self._colliders : list[CollisionComponent] = []
        self._clock = pygame.time.Clock()
        self._fps = 45
        self._width = 1300
        self._height = 700
        self._frame_time = (1 / self._fps)

 
    def load(self):
        pygame.init()
        self._window = pygame.display.set_mode((self._width, self._height))
        self._clock = pygame.time.Clock()
        ResourceManager.get().load_resources()
        ResourceManager.get().register_component("TextureComponent", TextureComponent())
        ResourceManager.get().register_component("CollisionComponent", CollisionComponent())
        
    def register_for_collision(self, collider : CollisionComponent):
        self._colliders.append(collider)

    def get_events(self) -> list[pygame.event.Event]:
        return self._events

    def set_active_scene(self, scene : Scene):
        self._active_scene = scene
        self._active_scene.load()
        pygame.display.update()
        pygame.display.flip()

    def get_active_scene(self) -> Scene:
        return self._active_scene
    
    def main_loop(self):
        running = True
        
        while running:
            self._clock.tick(self._fps)
            self._events.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self._events.append(event)
            
            self._active_scene.update(self._frame_time)
            self.check_collisions()
            self.draw()

    def check_collisions(self):
        if len(self._colliders) > 1:
            for i in range(len(self._colliders)):
                if self._colliders[i].get_response() == CollisionResponse.IGNORE:
                    continue
                for j in range(i + 1, len(self._colliders)):
                    if self._colliders[j].get_response() == CollisionResponse.IGNORE:
                        continue
                    collision_already_checked = False
                    if self._colliders[i].can_collide_with(self._colliders[j]):
                        if self.check_intersects(self._colliders[i].get_collision_bounds(), self._colliders[j].get_collision_bounds()):
                            collision_already_checked = True
                            self._colliders[i].on_collision(self._colliders[j])
                    if self._colliders[j].can_collide_with(self._colliders[i]):
                        if not collision_already_checked:
                            if self.check_intersects(self._colliders[i].get_collision_bounds(), self._colliders[j].get_collision_bounds()):
                                self._colliders[j].on_collision(self._colliders[i])
                self._colliders[i].update_collisions()

    def unload(self):
        pygame.quit()

    def draw(self):
        self._window.fill((0, 0, 0)) 
        self._active_scene.draw(self._window)
        pygame.display.flip()

    def get_window_size(self) -> tuple[int, int]:
        return self._width, self._height

    def check_intersects(self, rect1 : pygame.Rect, rect2 : pygame.Rect):
        return rect1.colliderect(rect2)
