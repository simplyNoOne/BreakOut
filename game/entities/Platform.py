
from engine import Entity, CollisionResponse, CollisionComponent, TextureComponent, CollisionMask, Engine
from engine.enums import Mobility
from game.components.PlayerActionsComponent import PlayerActionsComponent



class Platform(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._texture : TextureComponent = self.create_component_of_type("TextureComponent")
        self._collision : CollisionComponent = self.create_component_of_type("CollisionComponent")
        self._logic : PlayerActionsComponent = self.create_component_of_type("PlayerActionsComponent")


    def load(self):
        super().load()
        self._texture.set_texture("platform", 200, 20)
        self._collision.set_size(200, 8)
        self._collision.set_offset(0, 0)
        self._collision.set_collision_type(CollisionMask.MASK1)
        self._collision.set_response(CollisionResponse.OVERLAP)
        self._collision.set_mobility(Mobility.DYNAMIC)
        self._logic.set_bounds()
        Engine.get().register_for_collision(self._collision)
        window = Engine.get().get_window_size()
        self.x = (window[0] - self._texture.get_size()[0]) // 2
        self.y = 7 * window[1] // 8


    def unload(self):
        Engine.get().unregister_for_collision(self._collision)