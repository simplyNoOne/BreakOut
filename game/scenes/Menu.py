from engine.Scene import Scene

class Menu(Scene):
    def __init__(self):
        super().__init__()

    
    def populate_scene(self):
        self.add_entity("menu_entity")

    def load(self):
        super().load()
        
   