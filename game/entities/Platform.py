
from engine.Entity import Entity

class Platform(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._collision = self.create_component_of_type("CollisionComponent")
        self._texture = self.create_component_of_type("TextureComponent")
        self._logic = self.create_component_of_type("PlayerActionsComponent")


    def load(self):
        super().load()
        self._texture.set_texture("platform", 100, 150)
        self.x = 100
        self.y = 100


    def unload(self):
        pass

