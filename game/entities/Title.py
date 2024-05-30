from engine import Entity, Engine

class Title(Entity):
    def __init__(self):
        super().__init__()
        self._color = (220, 220, 220)

    def add_components(self):
        self._texture = self.create_component_of_type("TextureComponent")

    def load(self):
        super().load()
        self._texture.set_size(400, 100)
        self._texture.add_text("BreakOut", 100, self._color)
        window = Engine.get().get_window_size()
        self.x = window[0] // 2 - self._texture.get_size()[0] // 2
        self.y = 100
        

    def unload(self):
        super().unload()