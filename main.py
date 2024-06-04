
from engine import Engine, ResourceManager
from game import GameLevel, Menu, Leaderboard
from game import Platform, Ball, Wall, Brick
from game import LeaderboardEntity, LeaderboardComponent
from game import StatsDisplayComponent, StatsDisplay
from game import MenuButton, MenuEntity, MenuButtonsComponent, TextInputComponent, Title
from game import PlayerActionsComponent, WallBuilderComponent, BallBehaviorComponent, BrickBehaviorComponent
from game import GameManager

Engine.get().configure_window(1300, 700, 160, True, False)

Engine.get().load()

#------------------------------------



ResourceManager.get().register_scene("game_level", GameLevel())
ResourceManager.get().register_scene("menu", Menu())
ResourceManager.get().register_scene("leaderboard", Leaderboard())


ResourceManager.get().register_entity("platform", Platform())
ResourceManager.get().register_entity("ball", Ball())
ResourceManager.get().register_entity("brick", Brick())
ResourceManager.get().register_entity("wall", Wall())
ResourceManager.get().register_entity("menu_button", MenuButton())
ResourceManager.get().register_entity("menu_entity", MenuEntity())
ResourceManager.get().register_entity("leaderboard_entity", LeaderboardEntity())
ResourceManager.get().register_entity("stats_display", StatsDisplay())
ResourceManager.get().register_entity("title", Title())




ResourceManager.get().register_component("PlayerActionsComponent", PlayerActionsComponent())
ResourceManager.get().register_component("WallBuilderComponent", WallBuilderComponent())
ResourceManager.get().register_component("BallBehaviorComponent", BallBehaviorComponent())
ResourceManager.get().register_component("BrickBehaviorComponent", BrickBehaviorComponent())
ResourceManager.get().register_component("MenuButtonsComponent", MenuButtonsComponent())
ResourceManager.get().register_component("PlayerNameComponent", TextInputComponent())
ResourceManager.get().register_component("LeaderboardComponent", LeaderboardComponent())
ResourceManager.get().register_component("StatsDisplayComponent", StatsDisplayComponent())



GameManager.get().load()
                                                   



#------------------------------------

Engine.get().main_loop()

Engine.get().unload()

