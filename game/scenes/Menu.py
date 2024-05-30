from engine.Scene import Scene

class Menu(Scene):
    def __init__(self):
        super().__init__()

    
    def populate_scene(self):
        self.add_entity("menu_entity")
        self.add_entity("title")

    def load(self):
        super().load()
        
   