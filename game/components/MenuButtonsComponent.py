import pygame
from engine import Engine, EntityComponent, ResourceManager
from game.entities.MenuButton import MenuButton
from game.GameManager import GameManager


class MenuButtonsComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._play : MenuButton = None
        self._leaderboard : MenuButton = None
        self._quit : MenuButton = None
        self._buttons : list[MenuButton] = []
        self._active_button = 0
        self._on_play : list[function]= []
        self._on_leaderboard : list[function]= []
        self._on_quit : list[function]= []
        self._on_give_up_focus : list[function] = []
        self._focused : bool = False
        self._text_color = (220, 220, 220)
        self._font_size = 45
        self._button_shift = 300
        

    def load(self):
        super().load()
        self._play = ResourceManager.get().get_loaded_entity("menu_button")
        self._leaderboard = ResourceManager.get().get_loaded_entity("menu_button")
        self._quit = ResourceManager.get().get_loaded_entity("menu_button")
        self._buttons.append(self._leaderboard)
        self._buttons.append(self._play)
        self._buttons.append(self._quit)
        self._buttons_y = self._owner.y + 150
        self.setup_buttons()
        Engine.get().get_active_scene().add_existing_entity(self._play)
        Engine.get().get_active_scene().add_existing_entity(self._leaderboard)
        Engine.get().get_active_scene().add_existing_entity(self._quit)
        

    def bind_to_on_play(self, func):
        self._on_play.append(func)

    def bind_to_on_leaderboard(self, func):
        self._on_leaderboard.append(func)

    def bind_to_on_quit(self, func):
        self._on_quit.append(func)

    def bind_to_give_up_focus(self, func):
        self._on_give_up_focus.append(func)

    def setup_buttons(self):
        leader_txt = self._leaderboard.get_component("TextureComponent")
        leader_txt.add_text("Scores", self._font_size, self._text_color)
        self._leaderboard.x = self._owner.x - self._button_shift - leader_txt.get_size()[0]
        self._leaderboard.y = self._buttons_y
        play_txt = self._play.get_component("TextureComponent")
        play_txt.set_size(play_txt.get_size()[0] * 7 // 5, play_txt.get_size()[1] * 7 // 5)
        play_txt.add_text("Play", self._font_size + 10, self._text_color)
        self._play.x = self._owner.x - play_txt.get_size()[0] // 2
        self._play.y = self._buttons_y - 10
        quit_txt = self._quit.get_component("TextureComponent")
        quit_txt.add_text("Quit", self._font_size, self._text_color)
        self._quit.x = self._owner.x + self._button_shift
        self._quit.y = self._buttons_y

    def update(self, dt):
        super().update(dt)
        if not self._focused:
            return
        events = Engine.get().get_events()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._focused = False
                    for func in self._on_give_up_focus:
                        func()
                if event.key == pygame.K_LEFT:
                    self._active_button = self._active_button - 1 if self._active_button > 0 else 0
                if event.key == pygame.K_RIGHT:
                    self._active_button = self._active_button + 1 if self._active_button < len(self._buttons) - 1 else len(self._buttons) - 1
                if event.key == pygame.K_RETURN:
                    if self._buttons[self._active_button] == self._play:
                        for func in self._on_play:
                            func()
                    if self._buttons[self._active_button] == self._leaderboard:
                        for func in self._on_leaderboard:
                            func()
                    if self._buttons[self._active_button] == self._quit:
                        for func in self._on_quit:
                            func()
        
        self.refresh_buttons()


    def refresh_buttons(self):
        for button in self._buttons:
            button.get_component("TextureComponent").switch_texture("red")
        if self._focused:
            self._buttons[self._active_button].get_component("TextureComponent").switch_texture("green")

    def get_focus(self):
        self._active_button = 1
        self._focused = True
