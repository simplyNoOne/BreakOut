
from engine import Engine, ResourceManager
from game.scenes.GameLevel import GameLevel
from game.scenes.Menu import Menu
from game.entities.Platform import Platform
from game.entities.Ball import Ball
from game.entities.Wall import Wall
from game.entities.Brick import Brick
from game.components.PlayerActionsComponent import PlayerActionsComponent
from game.components.WallBuilderComponent import WallBuilderComponent
from game.components.BallBehaviorComponent import BallBehaviorComponent

Engine.get().load()

#------------------------------------

ResourceManager.get().register_scene("game_level", GameLevel())
ResourceManager.get().register_scene("menu", Menu())

ResourceManager.get().register_entity("platform", Platform())
ResourceManager.get().register_entity("ball", Ball())
ResourceManager.get().register_entity("brick", Brick())
ResourceManager.get().register_entity("wall", Wall())


ResourceManager.get().register_component("PlayerActionsComponent", PlayerActionsComponent())
ResourceManager.get().register_component("WallBuilderComponent", WallBuilderComponent())
ResourceManager.get().register_component("BallBehaviorComponent", BallBehaviorComponent())


                                                   
Engine.get().set_active_scene(ResourceManager.get().get_scene("game_level"))


#------------------------------------

Engine.get().main_loop()

Engine.get().unload()

