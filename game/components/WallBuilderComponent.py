from engine import EntityComponent, CollisionComponent
from engine import Engine, ResourceManager, random
from game.GameManager import GameManager
from game.enums import BrickType
import pygame

class WallBuilderComponent(EntityComponent):
    def __init__(self):
        super().__init__()

        
    def load(self):
        super().load()
        self._owner.x = 10
        self._owner.y = 50
        x, y = Engine.get().get_window_size()
        game_manager = GameManager.get()
        cols, rows = game_manager.get_cols(), game_manager.get_rows()
        self._harder_chance = game_manager.get_harder_chance()
        self._speedy_chance = game_manager.get_speedy_chance()
        self._bonus_chance = game_manager.get_bonus_chance()

        space = 10
        width = (x - space) // cols - space
        height = 20
        self.construct_wall(width, height, rows, cols, space)


    def construct_wall(self, brick_width, brick_height, rows, cols, space):
        for i in range(rows):
            for j in range(cols):
                brick = ResourceManager.get().get_loaded_entity("brick")
                collision_comp = brick.get_component("CollisionComponent")
                collision_comp.set_size(brick_width, brick_height )
                collision_comp.set_offset(0, 0)
                brick.get_component("TextureComponent").set_size(brick_width, brick_height)
                brick.x = self._owner.x + j * (brick_width + space)
                brick.y = self._owner.y + i * (brick_height + space)
                if random() < self._harder_chance:
                    brick.get_component("BrickBehaviorComponent").set_type(BrickType.HARD)
                elif random() < self._speedy_chance:
                    brick.get_component("BrickBehaviorComponent").set_type(BrickType.SPEEDY)
                elif random() < self._bonus_chance:
                    brick.get_component("BrickBehaviorComponent").set_type(BrickType.BONUS)
                Engine.get().register_for_collision(collision_comp)
                Engine.get().get_active_scene().add_existing_entity(brick)