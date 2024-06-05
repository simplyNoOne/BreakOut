from engine import EntityComponent, Engine
from game.GameManager import GameManager
from pygame import font


class StatsDisplayComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._score_label : str= "Score: " 
        self._color = (210,210,210)
        self._time = 0
        self._center_shift = 30

    def load(self):
        super().load()
        self._game_manager = GameManager.get()
        self._window = Engine.get().get_window_size()
        self._font = font.Font(None, 32)
        self._score_val : str = "0000"
        self._best_score : str = "Best Score: " + str(self._game_manager.get_players_best())
        self._time_label = "Time: "
        self._player_name = self._game_manager.get_player_name()
        self._best_score_surface = self._font.render(self._best_score, True, self._color)
        self._best_score_w = self._best_score_surface.get_width()
        self._best_score_x = self._owner.x
        self._score_surface = self._font.render(self._score_label + self._score_val, True, self._color)
        self._score_w = self._score_surface.get_width()
        self._score_x = self._window[0] - self._score_w - self._owner.x
        self._score_val = str(self._game_manager.get_score())
        self._player_name_surface = self._font.render(self._player_name, True, self._color)
        self._player_name_w = self._player_name_surface.get_width()
        self._player_name_x = self._window[0] // 2 - self._player_name_w - self._center_shift
        self._time = 0
        self._time_per_lvl = self._game_manager.get_play_time()
        self._time_surface = self._font.render(self._time_label + str(self._time_per_lvl), True, self._color)
        self._time_w = self._time_surface.get_width()
        self._time_x = self._window[0] // 2 +  self._center_shift
        
    def update(self, dt):
        self._score_val = str(self._game_manager.get_score())
        self._time += dt
        if self._time > self._time_per_lvl:
            self._time = self._time_per_lvl

    def draw(self, window):
        super().draw(window)
        self._score_surface = self._font.render(self._score_label + self._score_val, True, self._color)
        self._time_surface = self._font.render(self._time_label + str(self._time_per_lvl - int(self._time)), True, self._color)
        window.blit(self._best_score_surface, (self._best_score_x, self._owner.y))
        window.blit(self._score_surface, (self._score_x, self._owner.y))
        window.blit(self._player_name_surface, (self._player_name_x, self._owner.y))
        window.blit(self._time_surface, (self._time_x, self._owner.y))
