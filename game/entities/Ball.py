
from engine.Entity import Entity

class Ball(Entity):
    def __init__(self):
        super().__init__()

    def add_components(self):
        self._collision = self.create_component_of_type("CollisionComponent")
        self._texture = self.create_component_of_type("TextureComponent")


    def load(self):
        super().load()
        self._texture.set_texture("platform", 40, 40)
        self.x = 40
        self.y = 40


    def unload(self):
        pass

