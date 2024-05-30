

from engine.ResourceManager import ResourceManager
from engine.components.EntityComponent import EntityComponent
from pygame import Surface
import pygame

class TextureComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._texture : Surface = None
        self._width = 0
        self._height = 0
        self._text_x = 0
        self._text_y = 0
        self._text_surface = None


    def draw(self, screen : Surface):
        if self._texture:
            screen.blit(self._texture, (self._owner.x, self._owner.y ))
        if self._text_surface:
            screen.blit(self._text_surface, (self._owner.x + self._text_x, self._owner.y + self._text_y))


    def set_texture(self, name, width, height):
        texture = ResourceManager.get().get_texture(name)
        self._texture = pygame.transform.scale(texture, (width, height))
        self._width = width
        self._height = height
        
    def switch_texture(self, name):
        texture = ResourceManager.get().get_texture(name)
        self._texture = pygame.transform.scale(texture, (self._width, self._height))

    def set_size(self, width, height):
        if self._texture is not None:
            self._texture = pygame.transform.scale(self._texture, (width, height))
        self._width = width
        self._height = height

    def get_size(self):
        return self._width, self._height
    
    def add_text(self, text, font_size, color):
        self._font = pygame.font.Font(None, font_size)
        self._text_surface = self._font.render(text, True, color)
        w = self._text_surface.get_width()
        h = self._text_surface.get_height()
        self._text_x = (self._width - w) // 2
        self._text_y = (self._height - h) // 2

