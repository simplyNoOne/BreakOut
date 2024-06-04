
import functools
from engine import Entity, CollisionComponent, TextureComponent, CollisionResponse, CollisionMask, Engine, SoundComponent
from game.components.BrickBehaviorComponent import BrickBehaviorComponent
from game.enums import BrickType    


class Brick(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._texture : TextureComponent  = self.create_component_of_type("TextureComponent")
        self._collision : CollisionComponent = self.create_component_of_type("CollisionComponent")
        self._logic : BrickBehaviorComponent = self.create_component_of_type("BrickBehaviorComponent")
        self._sound : SoundComponent = self.create_component_of_type("SoundComponent")


    def load(self):
        super().load()
        self._texture.set_texture("standardBrick", 60, 45)
        self._collision.set_collision_type(CollisionMask.MASK3)
        self._collision.add_to_collision_mask(CollisionMask.MASK2)
        self._collision.bind_on_begin_ovelap(self._logic.on_overlap)
        self._collision.set_response(CollisionResponse.OVERLAP)
        self._logic.bind_on_type_changed(functools.partial(self.on_type_changed))
        self._sound.set_sound("break")
        self._sound.set_volume_percent(8)
  
    def unload(self):
        Engine.get().unregister_for_collision(self._collision)

    def on_type_changed(self, new_type : BrickType):
        if new_type == BrickType.SPEEDY:
            self._texture.switch_texture("speedyBrick")
        elif new_type == BrickType.BONUS:
            self._texture.switch_texture("bonusBrick")
        elif new_type == BrickType.HARD:
            self._texture.switch_texture("hardBrick")
        