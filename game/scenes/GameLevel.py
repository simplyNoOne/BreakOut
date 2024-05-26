from engine.Scene import Scene


class GameLevel(Scene):
    def __init__(self):
        super().__init__()

    def populate_scene(self):
        self.add_entity("platform")
        self.add_entity("ball")
        self.add_entity("wall")

    def load(self):
        super().load()


    def draw(self, window):
        super().draw(window)

    def update(self, dt):
        super().update(dt)
   