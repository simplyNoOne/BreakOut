
from engine import Engine, ResourceManager
from game.scenes.GameLevel import GameLevel
from game.scenes.Menu import Menu
from game.entities.Platform import Platform
from game.entities.Ball import Ball
from game.entities.Wall import Wall
from game.entities.Brick import Brick
from game.entities.MenuButton import MenuButton
from game.entities.MenuEntity import MenuEntity
from game.components.PlayerActionsComponent import PlayerActionsComponent
from game.components.WallBuilderComponent import WallBuilderComponent
from game.components.BallBehaviorComponent import BallBehaviorComponent
from game.components.BrickBehaviorComponent import BrickBehaviorComponent
from game.components.MenuButtonsComponent import MenuButtonsComponent

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


                                                   
Engine.get().set_active_scene("menu")


#------------------------------------

Engine.get().main_loop()

Engine.get().unload()

