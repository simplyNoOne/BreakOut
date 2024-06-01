from engine import Engine
from engine.Scene import Scene
from game.GameManager import GameManager  
from pygame import font 

class GameLevel(Scene):
    def __init__(self):
        super().__init__()
        self._level_info = "Level "

    def populate_scene(self):
        self.add_entity("ball")
        self.add_entity("platform")
        self.add_entity("wall")
        self.add_entity("stats_display")
        

    def load(self):
        super().load()
        self._level_info += str(GameManager.get().get_round()) 
        self._font = font.Font(None, 80)
        self._window_w, self._window_h = Engine.get().get_window_size()
        self._surface = self._font.render(self._level_info, True, (190,190,190))
        self._w = self._surface.get_width()
        

    def draw(self, window):
        window.blit(self._surface, ((self._window_w - self._w) // 2, self._window_h//2))
        super().draw(window)
        

    def update(self, dt):
        super().update(dt)
   