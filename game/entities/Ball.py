
from engine import Entity, CollisionComponent, TextureComponent, CollisionResponse, CollisionMask, Engine
from game.components.BallBehaviorComponent import BallBehaviorComponent


class Ball(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._collision : CollisionComponent = self.create_component_of_type("CollisionComponent")
        self._texture : TextureComponent  = self.create_component_of_type("TextureComponent")
        self._behavior : BallBehaviorComponent = self.create_component_of_type("BallBehaviorComponent")


    def load(self):
        super().load()
        self._texture.set_texture("ball", 15, 15)
        self._collision.set_size(13, 13)
        self._collision.set_offset(1, 1)
        self._collision.set_collision_type(CollisionMask.MASK2)
        self._collision.add_to_collision_mask(CollisionMask.MASK3)
        self._collision.set_response(CollisionResponse.OVERLAP)
        Engine.get().register_for_collision(self._collision)
        self.x = 540
        self.y = 630
