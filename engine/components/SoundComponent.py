
from engine.ResourceManager import ResourceManager
from engine.components.EntityComponent import EntityComponent
import pygame

class SoundComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._sound : pygame.mixer.Sound = None

    def play(self):
        self._sound.play()

    def set_sound(self, name):
        self._sound = ResourceManager.get().get_sound_effect(name)

    def set_volume_percent(self, volume):
        self._sound.set_volume(volume / 100)
