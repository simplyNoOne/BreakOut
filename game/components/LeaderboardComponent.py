import pygame
from engine import Engine, EntityComponent, ResourceManager
from game.database.DatabaseManager import DatabaseManager
from game.GameManager import GameManager
from game.entities.MenuButton import MenuButton

class LeaderboardComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._leaderboard = []
        self._back_button : MenuButton = None
        self._on_back = []
        self._font_size = 45
        self._color = (220, 220, 220)

    def load(self):
        super().load()
        self._back_button = ResourceManager.get().get_loaded_entity("menu_button")
        txt_comp = self._back_button.get_component("TextureComponent")
        txt_comp.switch_texture("green")
        txt_comp.add_text("Back", self._font_size, self._color)
        self._back_button.x = self._owner.x - txt_comp.get_size()[0] // 2
        self._back_button.y = (5 * self._owner.y ) // 3
        Engine.get().get_active_scene().add_existing_entity(self._back_button)
        self._font = pygame.font.Font(None, 50)
        self.populate_leaderboard()


    def populate_leaderboard(self):
        entries = GameManager.get().get_leaderboard()
        for i, entry in enumerate(entries):
            text = f"{i + 1}. {entry.player.name} - {entry.score}"
            self._leaderboard.append(text)


    def update(self, dt):
        super().update(dt)

        events = Engine.get().get_events()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    for func in self._on_back:
                        func()


    def draw(self, window):
        super().draw(window)
        for i, entry in enumerate(self._leaderboard):
            text = self._font.render(entry, True, (255, 255, 255))
            window.blit(text, (self._owner.x - 100, self._owner.y - 300 + i * 45))


    def bind_to_back_button(self, func):
        self._on_back.append(func)
