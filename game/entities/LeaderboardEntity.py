from engine import Entity, Engine, ResourceManager
from game.components.LeaderboardComponent import LeaderboardComponent
from game.GameManager import GameManager


class LeaderboardEntity(Entity):
    def __init__(self):
        super().__init__()
        self._color = (220, 220, 220)
        self._font_size = 80


    def add_components(self):
        self._leaderboard_actions : LeaderboardComponent = self.create_component_of_type("LeaderboardComponent")
        self._title = self.create_component_of_type("TextureComponent")

    def load(self):
        window_size = Engine.get().get_window_size()
        self.x = window_size[0] // 2
        self.y = window_size[1] // 7
        super().load()
        self._title.add_text("Leaderboard", self._font_size, self._color)
        self._leaderboard_actions.bind_to_back_button(GameManager.get().back_to_menu)

    def unload(self):
        super().unload()
