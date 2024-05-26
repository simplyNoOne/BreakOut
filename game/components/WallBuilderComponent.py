from engine import EntityComponent, CollisionComponent
from engine import Engine, ResourceManager
import pygame

class WallBuilderComponent(EntityComponent):
    def __init__(self):
        super().__init__()

        
    def load(self):
        super().load()
        self.construct_wall(35, 4, 10, 20)


    def construct_wall(self, brick_width, brick_height, rows, cols):
        for i in range(rows):
            for j in range(cols):
                brick = ResourceManager.get().get_loaded_entity("brick")
                collision_comp = brick.get_component("CollisionComponent")
                collision_comp.set_size(brick_width + 2, brick_height + 2)
                collision_comp.set_offset(-1, -1)
                Engine.get().register_for_collision(collision_comp)
                brick.get_component("TextureComponent").set_size(brick_width, brick_height)
                brick.x = self._owner.x + j * (brick_width + 40)
                brick.y = self._owner.y + i * (brick_height + 40)
                Engine.get().get_active_scene().add_existing_entity(brick)