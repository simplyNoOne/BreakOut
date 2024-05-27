import pygame
from engine import Engine, EntityComponent, ResourceManager
from game.entities.MenuButton import MenuButton

class MenuButtonsComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._play : MenuButton = None
        self._quit : MenuButton = None
        self._buttons : list[MenuButton] = []
        self._active_button = 0
        

    def load(self):
        super().load()
        self._play = ResourceManager.get().get_loaded_entity("menu_button")
        self._quit = ResourceManager.get().get_loaded_entity("menu_button")
        self._buttons.append(self._play)
        self._buttons.append(self._quit)
        self.setup_buttons()
        Engine.get().get_active_scene().add_existing_entity(self._play)
        Engine.get().get_active_scene().add_existing_entity(self._quit)
        
    def setup_buttons(self):
        self._play.x = self._owner.x - 300 - self._play.get_component("TextureComponent").get_size()[0]
        self._play.y = self._owner.y
        self._quit.x = self._owner.x + 300
        self._quit.y = self._owner.y
        self._play.get_component("TextureComponent").switch_texture("green")

    def update(self, dt):
        super().update(dt)
        events = Engine.get().get_events()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Engine.get().quit_game()
                if event.key == pygame.K_LEFT:
                    self._active_button = self._active_button - 1 if self._active_button > 0 else 0
                if event.key == pygame.K_RIGHT:
                    self._active_button = self._active_button + 1 if self._active_button < len(self._buttons) - 1 else len(self._buttons) - 1
                if event.key == pygame.K_RETURN:
                    if self._buttons[self._active_button] == self._play:
                        Engine.get().set_active_scene("game_level")
                    if self._buttons[self._active_button] == self._quit:
                        Engine.get().quit_game()
        
        self.refresh_buttons()


    def refresh_buttons(self):
        for button in self._buttons:
            button.get_component("TextureComponent").switch_texture("red")
        self._buttons[self._active_button].get_component("TextureComponent").switch_texture("green")