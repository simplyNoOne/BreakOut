
from engine import Entity, CollisionComponent, TextureComponent, CollisionResponse, CollisionMask


class Brick(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._collision : CollisionComponent = self.create_component_of_type("CollisionComponent")
        self._texture : TextureComponent  = self.create_component_of_type("TextureComponent")


    def load(self):
        super().load()
        self._texture.set_texture("standardBrick", 45, 15)
        self._collision.set_collision_type(CollisionMask.MASK3)
        self._collision.add_to_collision_mask(CollisionMask.MASK2)
        self._collision.set_response(CollisionResponse.BLOCK)
  