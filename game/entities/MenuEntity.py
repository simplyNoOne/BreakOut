from engine import Entity,  Engine
from game.components.MenuButtonsComponent import MenuButtonsComponent
from game.components.PlayerNameComponent import PlayerNameComponent
from game.GameManager import GameManager

class MenuEntity(Entity):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def add_components(self):
        self._buttons_actions : MenuButtonsComponent = self.create_component_of_type("MenuButtonsComponent")
        self._player_name_actions : PlayerNameComponent = self.create_component_of_type("PlayerNameComponent")

    def load(self):
        window_size = Engine.get().get_window_size()
        self.x = window_size[0] // 2
        self.y = 3 * window_size[1] // 4
        super().load()
        self._buttons_actions.bind_to_on_play(self._player_name_actions.game_starting)
        self._buttons_actions.bind_to_on_play(GameManager.get().start_game)

    def unload(self):
        super().unload()