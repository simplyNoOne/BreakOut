
from engine import Entity, CollisionResponse, CollisionComponent, TextureComponent, CollisionMask, Engine
from game.components.PlayerActionsComponent import PlayerActionsComponent



class Platform(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._collision : CollisionComponent = self.create_component_of_type("CollisionComponent")
        self._texture : TextureComponent = self.create_component_of_type("TextureComponent")
        self._logic : PlayerActionsComponent = self.create_component_of_type("PlayerActionsComponent")


    def load(self):
        super().load()
        self._texture.set_texture("platform", 100, 10)
        self._collision.set_size(102, 12)
        self._collision.set_offset(-1, -1)
        self._collision.set_collision_type(CollisionMask.MASK1)
        self._collision.add_to_collision_mask(CollisionMask.MASK2)
        self._collision.set_response(CollisionResponse.OVERLAP)
        self._collision.bind_on_begin_ovelap(self._logic.on_overlap)
        Engine.get().register_for_collision(self._collision)
        self.x = 300
        self.y = 630


    def unload(self):
        pass

