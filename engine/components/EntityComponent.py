

from abc import ABC


class EntityComponent(ABC):
    
    def __init__(self):
        self._owner = None
        self._name = "EntityComponent"

    def update(self, dt):
        pass

    def draw(self, window):
        pass

    def load(self):
        pass

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name

