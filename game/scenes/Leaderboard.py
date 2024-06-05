from engine import Scene


class Leaderboard(Scene):
    def __init__(self):
        super().__init__()

    def populate_scene(self):
        self.add_entity("leaderboard_entity")

    def load(self):
        super().load()
        
