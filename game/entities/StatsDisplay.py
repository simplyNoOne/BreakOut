from engine import Entity

class StatsDisplay(Entity):
    def __init__(self):
        super().__init__()
        self.x = 30
        self.y = 15

    def add_components(self):
        self.create_component_of_type("StatsDisplayComponent")

    def load(self):
        super().load()

    def unload(self):
        super().unload()