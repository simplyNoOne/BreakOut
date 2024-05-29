from engine import Entity, Engine, ResourceManager
from game.components.LeaderboardComponent import LeaderboardComponent
from game.GameManager import GameManager


class LeaderboardEntity(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._leaderboard_actions : LeaderboardComponent = self.create_component_of_type("LeaderboardComponent")

    def load(self):
        window_size = Engine.get().get_window_size()
        self.x = window_size[0] // 2
        self.y = window_size[1] // 2
        super().load()
        self._leaderboard_actions.bind_to_back_button(GameManager.get().back_to_menu)

    def unload(self):
        super().unload()
