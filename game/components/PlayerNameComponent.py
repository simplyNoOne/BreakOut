import pygame
from engine import Engine, EntityComponent, ResourceManager
from game.entities.MenuButton import MenuButton
from game.GameManager import GameManager
from pygame import font, Rect


class PlayerNameComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._text = ""
        self._input_box : Rect = None

        

    def load(self):
        super().load()
        self._input_box = Rect(self._owner.x, self._owner.y - 200, 140, 60)
        self._font = pygame.font.Font(None, 50)


    def update(self, dt):
        super().update(dt)
        events = Engine.get().get_events()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += event.unicode


    def game_starting(self):
        GameManager.get().set_player(self._text)
        

    def draw(self, window):
        super().draw(window)
        txt_surface = self._font.render(self._text, True, (230,230,230))
        width = max(200, txt_surface.get_width() + 10)
        self._input_box.w = width
        self._input_box.x = self._owner.x - width // 2
        window.blit(txt_surface, (self._input_box.x + 5, self._input_box.y + 5))
        pygame.draw.rect(window, (200,200,200), self._input_box, 2)

