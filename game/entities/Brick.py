
from engine import Entity, CollisionComponent, TextureComponent, CollisionResponse, CollisionMask, Engine
from game.components.BrickBehaviorComponent import BrickBehaviorComponent
from game.GameManager import GameManager
class Brick(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._texture : TextureComponent  = self.create_component_of_type("TextureComponent")
        self._collision : CollisionComponent = self.create_component_of_type("CollisionComponent")
        self._logic : BrickBehaviorComponent = self.create_component_of_type("BrickBehaviorComponent")


    def load(self):
        super().load()
        self._texture.set_texture("standardBrick", 60, 45)
        self._collision.set_collision_type(CollisionMask.MASK3)
        self._collision.add_to_collision_mask(CollisionMask.MASK2)
        self._collision.bind_on_begin_ovelap(self._logic.on_overlap)
        self._collision.set_response(CollisionResponse.OVERLAP)
  
    def unload(self):
        Engine.get().unregister_for_collision(self._collision)