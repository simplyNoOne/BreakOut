from engine.Scene import Scene

class Menu(Scene):
    def __init__(self):
        super().__init__()



    def draw(self, window):
        pass

    def update(self, dt):
        pass

    
    def populate_scene(self):
        self.add_entity("platform")

    def load(self):
        super().load()
        
   