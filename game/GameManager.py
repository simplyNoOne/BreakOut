from .database.DatabaseManager import DatabaseManager
from .database.Model import Player
from engine import Engine

class GameManager:
    _instance = None


    @staticmethod
    def get():
        if not GameManager._instance:
            GameManager._instance = GameManager()
        return GameManager._instance

    def __init__(self):
        self._db : DatabaseManager= DatabaseManager()
        self._round : int= 0
        self._score : int = 0
        self._player : Player = None
        self._start_platform_vel = 900
        self._start_ball_vel = 450
        self._ball_vel_incr = 25
        self._platform_vel_incr = 40
        self._start_cols = 7
        self._start_rows = 4
        self._bricks = self._start_rows * self._start_cols
        self._bricks_left = self._bricks
        self._scene : str = "menu"
        self._loaded = False
        self._music_loudness = 10
        self._level_being_switched = False

    def log_player(self, player_name, password):
        if player_name == "":
            player_name = "Anonymous"
        if player_name == "Anonymous":
            password = ""
        self._player = Player.get_or_none(Player.name == player_name)
        if not self._player:
            self._player = Player.create(name=player_name, password=password)
            self._db.set_player_score(self._player, 0)
        else:
            if self._player.password != password:
                self._player = None 
                return
            

    def refresh_bricks(self):
        self._bricks = self.get_cols() * self.get_rows()
        self._bricks_left = self._bricks            

    def load(self):
        if self._loaded:
            return
        self._loaded = True
        self._db.load("database")
        Engine.get().set_active_scene(self._scene)
        Engine.get().play_music("menu", self._music_loudness)

    def start_game(self):
        if not self._player:
            return
        self._round = 1
        self.enter_game_level()
   
    def on_won(self):
        self._level_being_switched = True
        self._round += 1
        Engine.get().set_function_delay(self.enter_game_level, 1.5)

    def on_lost(self):
        if self._level_being_switched:
            return
        self._level_being_switched = True
        self.update_db()
        Engine.get().set_function_delay(self.exit_game_level, 2)
        

    def enter_game_level(self):
        Engine.get().wait(1.5)
        self.refresh_bricks()
        self._scene = "game_level"
        Engine.get().set_active_scene(self._scene)
        Engine.get().play_music("game_level", self._music_loudness)
        self._level_being_switched = False


    def exit_game_level(self):
        self._round = 0
        self._score = 0
        self._scene = "menu"
        Engine.get().resume()
        Engine.get().set_active_scene(self._scene)
        Engine.get().play_music("menu", self._music_loudness)
        self._level_being_switched = False

    def to_leaderboard(self):
        if not self._player:
            return
        self._scene = "leaderboard"
        Engine.get().set_active_scene(self._scene)

    def back_to_menu(self):
        self._scene = "menu"
        Engine.get().set_active_scene(self._scene)

    def update_db(self):
        former_best = self._db.get_player_score(self._player)
        if former_best > self._score:
            return
        self._db.set_player_score(self._player, self._score)
        

    def get_round(self):
        return self._round

    def get_cols(self):
        return self._start_cols + (self._round // 2)
    
    def get_rows(self):
        return self._start_rows
    
    def get_ball_vel(self):
        return self._start_ball_vel + (self._round * self._ball_vel_incr)
    
    def get_platform_vel(self):
        return self._start_platform_vel + ((self._round // 2) * self._platform_vel_incr)

    def get_score(self):
        return self._score
    
    def get_speedy_chance(self):
        return (self._round // 2) * 0.13
    
    def get_bonus_chance(self):
        return (self._round // 3) * 0.06

    def get_harder_chance(self):
        return (self._round // 4) * 0.15

    def brick_broken(self, points : int):
        self._score += points
        self._bricks_left -= 1
        if self._bricks_left == 0:
            self.on_won()

    def get_player_name(self):
        if self._player:    
            return self._player.name
        return ""
    
    def get_player_password(self):
        if self._player:
            return self._player.password
        return ""

    def get_leaderboard(self):

        res = self._db.get_scores(10)
        print(res)
        for r in res :
            print(r)
        return res
    
    def get_players_best(self):
        return self._db.get_player_score(self._player)


    def delete_active_player(self):
        if self._player:
            if self._player.name == "Anonymous":
                return
            self._db.delete_player(self._player)
            self.log_player("", "")
            self.to_leaderboard()

    def player_anonymous(self):
        return self._player.name == "Anonymous"