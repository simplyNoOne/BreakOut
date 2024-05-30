from engine import EntityComponent, Engine
from engine import CollisionComponent
from game.GameManager import GameManager
from game.enums import BrickType 

class BrickBehaviorComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._broken = False
        self._brick_type : BrickType = BrickType.NORMAL


    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        if other._owner.get_name() == "ball":
            if not self._broken:
                Engine.get().get_active_scene().remove_entity(self._owner)
                GameManager.get().brick_broken(self._brick_type.value)
                self._broken = True
        

    def set_type(self, value : BrickType):
        self._brick_val = value

