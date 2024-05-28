
from engine import Engine, ResourceManager
from game import GameLevel, Menu
from game import Platform, Ball, Wall, Brick
from game import MenuButton, MenuEntity, MenuButtonsComponent, PlayerNameComponent
from game import PlayerActionsComponent, WallBuilderComponent, BallBehaviorComponent, BrickBehaviorComponent
from game import GameManager

Engine.get().load()

#------------------------------------



ResourceManager.get().register_scene("game_level", GameLevel())
ResourceManager.get().register_scene("menu", Menu())

ResourceManager.get().register_entity("platform", Platform())
ResourceManager.get().register_entity("ball", Ball())
ResourceManager.get().register_entity("brick", Brick())
ResourceManager.get().register_entity("wall", Wall())
ResourceManager.get().register_entity("menu_button", MenuButton())
ResourceManager.get().register_entity("menu_entity", MenuEntity())



ResourceManager.get().register_component("PlayerActionsComponent", PlayerActionsComponent())
ResourceManager.get().register_component("WallBuilderComponent", WallBuilderComponent())
ResourceManager.get().register_component("BallBehaviorComponent", BallBehaviorComponent())
ResourceManager.get().register_component("BrickBehaviorComponent", BrickBehaviorComponent())
ResourceManager.get().register_component("MenuButtonsComponent", MenuButtonsComponent())
ResourceManager.get().register_component("PlayerNameComponent", PlayerNameComponent())


GameManager.get().load()
                                                   



#------------------------------------

Engine.get().main_loop()

Engine.get().unload()

