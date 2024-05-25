

from abc import ABC, abstractmethod


class EntityComponent(ABC):
    
    def __init__(self):
        self._owner = None

    def update(self, dt):
        pass

    def draw(self, window):
        pass

    def load(self):
        pass
