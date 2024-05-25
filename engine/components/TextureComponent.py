

from engine.ResourceManager import ResourceManager
from engine.components.EntityComponent import EntityComponent
from pygame import Rect, Surface

class TextureComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._texture : Surface = None
        self._width = 0
        self._height = 0

    def draw(self, screen : Surface):
        screen.blit(self._texture, (self._owner.x, self._owner.y ))


    def set_texture(self, name, width, height):
        texture = ResourceManager.get().get_texture(name)
        self._texture = texture
        self._width = width
        self._height = height