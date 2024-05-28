from engine import EntityComponent, CollisionComponent
from engine import Engine, ResourceManager
from game.GameManager import GameManager
import pygame

class WallBuilderComponent(EntityComponent):
    def __init__(self):
        super().__init__()

        
    def load(self):
        super().load()
        self._owner.x = 10
        self._owner.y = 10
        x, y = Engine.get().get_window_size()
        cols, rows = GameManager.get().get_cols(), GameManager.get().get_rows()
        space = 10
        width = (x - space) // cols - space
        height = 20
        self.construct_wall(width, height, rows, cols, space)


    def construct_wall(self, brick_width, brick_height, rows, cols, space):
        for i in range(rows):
            for j in range(cols):
                brick = ResourceManager.get().get_loaded_entity("brick")
                collision_comp = brick.get_component("CollisionComponent")
                collision_comp.set_size(brick_width + 2, brick_height + 2)
                collision_comp.set_offset(-1, -1)
                Engine.get().register_for_collision(collision_comp)
                brick.get_component("TextureComponent").set_size(brick_width, brick_height)
                brick.x = self._owner.x + j * (brick_width + space)
                brick.y = self._owner.y + i * (brick_height + space)
                Engine.get().get_active_scene().add_existing_entity(brick)