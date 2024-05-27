from engine import EntityComponent, Engine
from engine import CollisionComponent

class BrickBehaviorComponent(EntityComponent):
    def __init__(self):
        super().__init__()



    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        if other._owner.get_name() == "ball":
            Engine.get().get_active_scene().remove_entity(self._owner)
        

