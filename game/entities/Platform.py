
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
        self._texture.set_texture("platform", 200, 20)
        self._collision.set_size(202,22)
        self._collision.set_offset(-1, -1)
        self._collision.set_collision_type(CollisionMask.MASK1)
        self._collision.add_to_collision_mask(CollisionMask.MASK2)
        self._collision.set_response(CollisionResponse.OVERLAP)
        self._collision.bind_on_begin_ovelap(self._logic.on_overlap)
        Engine.get().register_for_collision(self._collision)
        window = Engine.get().get_window_size()
        self.x = window[0] // 2
        self.y = 7 * window[1] // 8


    def unload(self):
        Engine.get().unregister_for_collision(self._collision)