from abc import ABC, abstractmethod


from engine import Entity
from engine.ResourceManager import ResourceManager

class Scene(ABC):
    @abstractmethod
    def __init__(self):
        self._entities : list[Entity] = []

    @abstractmethod
    def load(self):
        self.populate_scene()
        for entity in self._entities:
            entity.load()
        
    @abstractmethod
    def populate_scene(self):
        pass

    def draw(self, window):
        for entity in self._entities:
            entity.draw(window)

    def update(self, dt):
        for entity in self._entities:
            entity.update(dt)

    
    def add_existing_entity(self, entity: Entity):
        self._entities.append(entity)

    def add_entity(self, name: str):
        entity = ResourceManager.get().get_entity(name)
        self._entities.append(entity)

    def remove_entity(self, entity: Entity):
        self._entities.remove(entity)