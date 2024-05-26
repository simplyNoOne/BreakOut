import copy
import os
import json
import pygame
from engine.components.EntityComponent import EntityComponent

class ResourceManager:
    _instance = None

    def __init__(self):
        self._components = {}
        self._entities = {}
        self._textures = {}
        self._scenes = {}
        

    def get():
        if not ResourceManager._instance:
            ResourceManager._instance = ResourceManager()
        return ResourceManager._instance

    def load_resources(self):
        self.load_textures_from_path("resources/textures")
        

    def load_textures_from_path(self, path):
        for filename in os.listdir(path):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                texture_name = os.path.splitext(filename)[0]
                texture_path = os.path.join(path, filename)
                self._textures[texture_name] = pygame.image.load(texture_path)


    def register_component(self, name : str, component : EntityComponent):
        component.set_name(name)
        self._components[name] = component

    def get_component(self, name):
        return copy.deepcopy(self._components[name])
    
    def register_entity(self, name, entity):
        self._entities[name] = entity
    
    def get_loaded_entity(self, name : str):
        to_ret = copy.deepcopy(self._entities[name])
        to_ret.load()
        return to_ret
    
    def get_entity(self, name):
        return copy.deepcopy(self._entities[name])
    
    def register_scene(self, name, scene):
        self._scenes[name] = scene

    def get_scene(self, name):
        return copy.deepcopy(self._scenes[name])
    
    def get_texture(self, name):
        return self._textures[name] 
    


