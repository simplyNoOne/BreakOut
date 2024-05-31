from engine import EntityComponent, Engine
from engine import CollisionComponent
from game.GameManager import GameManager
from game.enums import BrickType 

class BrickBehaviorComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._self_hits_left = 1
        self._brick_type : BrickType = BrickType.NORMAL
        self._on_type_changed = []


    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        if other._owner.get_name() == "ball":
            self._self_hits_left -= 1
            if self._self_hits_left == 0:
                self._owner.get_component("SoundComponent").play()
                Engine.get().get_active_scene().remove_entity(self._owner)
                GameManager.get().brick_broken((self._brick_type.value + 1) // 2 )
            else:
                self._owner.get_component("TextureComponent").switch_texture("bonusBrick")


    def set_type(self, value : BrickType):
        self._brick_type = value
        if self._brick_type == BrickType.HARD:
            self._self_hits_left = 2
        for func in self._on_type_changed:
            func(value)

    def does_change_ball_speed(self):
        return self._brick_type == BrickType.SPEEDY

    def bind_on_type_changed(self, func : callable):
        self._on_type_changed.append(func)

