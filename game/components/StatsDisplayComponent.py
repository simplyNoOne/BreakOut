from engine import EntityComponent, Engine
from game.GameManager import GameManager
from pygame import font

class StatsDisplayComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._score_label : str= "Score: " 

    def load(self):
        super().load()
        self._game_manager = GameManager.get()
        self._window = Engine.get().get_window_size()
        self._font = font.Font(None, 32)
        self._score_val : str = "0000"
        self._best_score : str = "Best Score: " + str(self._game_manager.get_players_best())
        self._best_score_surface = self._font.render(self._best_score, True, (210,210,210))
        self._best_score_w = self._best_score_surface.get_width()
        self._best_score_x = self._owner.x
        self._score_surface = self._font.render(self._score_label + self._score_val, True, (210,210,210))
        self._score_w = self._score_surface.get_width()
        self._score_x = self._window[0] - self._score_w - self._owner.x
        

    def update(self, dt):
        self._score_val = str(self._game_manager.get_score())

    def draw(self, window):
        super().draw(window)
        self._score_surface = self._font.render(self._score_label + self._score_val, True, (210,210,210))
        window.blit(self._best_score_surface, (self._best_score_x, self._owner.y))
        window.blit(self._score_surface, (self._score_x, self._owner.y))