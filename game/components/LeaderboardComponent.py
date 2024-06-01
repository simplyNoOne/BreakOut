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
        self._on_delete = []
        self._font_size = 40
        self._color = (220, 220, 220)
        self._shift = 200
        self._buttons = []

    def load(self):
        super().load()
        self._back_button = ResourceManager.get().get_loaded_entity("menu_button")
        self._delete_button = ResourceManager.get().get_loaded_entity("menu_button")
        buttons_y = Engine.get().get_window_size()[1] - self._owner.y - self._back_button.get_component("TextureComponent").get_size()[1] // 2
        back_txt_comp = self._back_button.get_component("TextureComponent")
        back_txt_comp.switch_texture("green")
        back_txt_comp.add_text("Back", self._font_size, self._color)
        delete_txt_comp = self._delete_button.get_component("TextureComponent")
        delete_txt_comp.add_text("Delete", self._font_size, self._color)
        self._back_button.x = self._owner.x - back_txt_comp.get_size()[0] - self._shift
        self._back_button.y = buttons_y
        self._delete_button.x = self._owner.x + self._shift
        self._delete_button.y = buttons_y
        self._buttons.append(self._back_button)
        self._buttons.append(self._delete_button)
        self._active_button = 0

        Engine.get().get_active_scene().add_existing_entity(self._back_button)
        Engine.get().get_active_scene().add_existing_entity(self._delete_button)

        self._font = pygame.font.Font(None, self._font_size)
        self.populate_leaderboard()


    def populate_leaderboard(self):
        GameManager.get().update_db()
        entries = GameManager.get().get_leaderboard()
        for i, entry in enumerate(entries):
            print(entry.player.name)
            if entry.player.name == GameManager.get().get_player_name():
                text = (f"{str(i + 1).zfill(2)}.    {entry.player.name} (You)", f"{13*" "}{entry.score}")
            else:
                text = (f"{str(i + 1).zfill(2)}.    {entry.player.name}", f"{13*" "}{entry.score}")
            self._leaderboard.append(text)


    def update(self, dt):
        super().update(dt)

        events = Engine.get().get_events()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self._buttons[self._active_button] == self._back_button:
                        for func in self._on_back:
                            func()
                    if self._buttons[self._active_button] == self._delete_button:
                        for func in self._on_delete:
                            func()


                if event.key == pygame.K_LEFT:
                    self._active_button = self._active_button - 1 if self._active_button > 0 else 0
                if event.key == pygame.K_RIGHT:
                    self._active_button = self._active_button + 1 if self._active_button < len(self._buttons) - 1 else len(self._buttons) - 1
                
        
        self.refresh_buttons()


    def refresh_buttons(self):
        for button in self._buttons:
            button.get_component("TextureComponent").switch_texture("red")
        
        self._buttons[self._active_button].get_component("TextureComponent").switch_texture("green")


    def draw(self, window):
        super().draw(window)
        lengths = []
        renders = []
        for i, entry in enumerate(self._leaderboard):
            text_name = self._font.render(entry[0], True, self._color)
            text_score = self._font.render(entry[1], True, self._color)
            lengths.append(text_name.get_width() + text_score.get_width())
            renders.append((text_name, text_score))
        
        max_length = max(lengths)
        for i, entry in enumerate(renders):
            window.blit(entry[0], (self._owner.x - max_length // 2, self._owner.y + 50 + i * 40))
            window.blit(entry[1], (self._owner.x + (max_length - entry[1].get_width()) - max_length // 2, self._owner.y + 50 + i * 40))


    def bind_to_back_button(self, func):
        self._on_back.append(func)

    def bind_to_delete_button(self, func):
        self._on_delete.append(func)
