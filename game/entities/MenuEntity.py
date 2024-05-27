from engine import Entity,  Engine

class MenuEntity(Entity):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def add_components(self):
        self._buttons_actions = self.create_component_of_type("MenuButtonsComponent")

    def load(self):
        window_size = Engine.get().get_window_size()
        self.x = window_size[0] // 2
        self.y = 3 * window_size[1] // 4
        super().load()

    def unload(self):
        super().unload()