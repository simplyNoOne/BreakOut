
from engine import Entity


class Wall(Entity):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def add_components(self):
        self._wall_builder = self.create_component_of_type("WallBuilderComponent")

    def load(self):
        super().load()

    def unload(self):
        super().unload()