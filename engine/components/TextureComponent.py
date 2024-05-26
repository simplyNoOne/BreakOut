

from engine.ResourceManager import ResourceManager
from engine.components.EntityComponent import EntityComponent
from pygame import Rect, Surface
import pygame

class TextureComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._texture : Surface = None


    def draw(self, screen : Surface):
        screen.blit(self._texture, (self._owner.x, self._owner.y ))


    def set_texture(self, name, width, height):
        texture = ResourceManager.get().get_texture(name)
        self._texture = pygame.transform.scale(texture, (width, height))
        

    def set_size(self, width, height):
        self._texture = pygame.transform.scale(self._texture, (width, height))