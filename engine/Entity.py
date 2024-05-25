from abc import ABC, abstractmethod
from engine.components.EntityComponent import EntityComponent
from engine.ResourceManager import ResourceManager

class Entity(ABC):
    @abstractmethod
    def __init__(self):
        self._components : list[EntityComponent] = []
        self.x = 0
        self.y = 0

    @abstractmethod
    def load(self):
        self.add_components()
        for c in self._components:
            c.load()
        
    @abstractmethod
    def add_components(self):
        pass

    def draw(self, window):
        for c in self._components:
            c.draw(window)

    def update(self, dt):
        for c in self._components:
            c.update(dt)

    def create_component_of_type(self, type: str) -> EntityComponent:
        component = ResourceManager.get().get_component(type)
        component._owner = self
        self._components.append(component)
        return component

    @abstractmethod
    def unload(self):
        pass
