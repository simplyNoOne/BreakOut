from abc import ABC, abstractmethod
from engine.components.EntityComponent import EntityComponent
from engine.ResourceManager import ResourceManager
from engine.components.CollisionComponent import CollisionComponent

class Entity(ABC):
    @abstractmethod
    def __init__(self):
        self._components : list[EntityComponent] = []
        self.x = 0
        self.y = 0
        self._loaded = False
        self._name = "Entity"

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name):
        self._name = name

    @abstractmethod
    def load(self):
        self._loaded = True
        self.add_components()
        for c in self._components:
            c.load()

    def not_loaded(self) -> bool:
        return not self._loaded
        
    @abstractmethod
    def add_components(self):
        pass

    def draw(self, window):
        for c in self._components:
            c.draw(window)

    def update(self, dt):
        for c in self._components:
            c.update(dt)

    def get_component(self, type: str) -> EntityComponent:
        for c in self._components:
            if c.get_name() == type:
                return c
        return None

    def create_component_of_type(self, type: str) -> EntityComponent:
        component : EntityComponent = ResourceManager.get().get_component(type)
        component._owner = self
        self._components.append(component)
        return component

    @abstractmethod
    def unload(self):
        pass
