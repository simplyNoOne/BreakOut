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

    def get_components_to_register_for_collision(self):
        colliders = []
        for c in self._components:
            if isinstance(c, CollisionComponent):
                colliders.append(c)
        return colliders
    
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

    def unload(self):
        pass
