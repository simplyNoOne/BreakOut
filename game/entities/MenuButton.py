from engine import Entity, TextureComponent, Engine

class MenuButton(Entity):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def add_components(self):
        self._texture : TextureComponent = self.create_component_of_type("TextureComponent")

    def load(self):
        super().load()
        self._texture.set_texture("red", 200, 50)
       

    def unload(self):
        super().unload()