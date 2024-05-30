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
        self._start_ball_vel = 200
        self._ball_vel_incr = 50
        self._platform_vel_incr = 50
        self._start_cols = 7
        self._start_rows = 4
        self._bricks = self._start_rows * self._start_cols
        self._bricks_left = self._bricks
        self._scene : str = "menu"
        self._loaded = False

    def log_player(self, player_name, password):
        if player_name == "":
            player_name = "Anonymous"
            password = ""
        self._player = Player.get_or_none(Player.name == player_name)
        if not self._player:
            self._player = Player.create(name=player_name, password=password)
            self._db.set_player_score(self._player, 0)
        else:
            if self._player.password != password:
                self._player = None
                return
        self.start_game()

    def refresh_bricks(self):
        self._bricks = self.get_cols() * self.get_rows()
        self._bricks_left = self._bricks            


    def load(self):
        if self._loaded:
            return
        self._loaded = True
        self._db.load("database")
        Engine.get().set_active_scene(self._scene)

    def start_game(self):
        self._round = 1
        self.refresh_bricks()
        self._scene = "game_level"
        Engine.get().set_active_scene(self._scene)

    def reset_game(self):
        self._score = 0
        self._round = 0
        self.refresh_bricks()
        self._player = None

    def on_lost(self):
        self.update_db()
        self._scene = "menu"
        self.reset_game()
        Engine.get().set_active_scene(self._scene)

    def to_leaderboard(self):
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
        self._db.remove_excess(10)

    def get_round(self):
        return self._round

    def get_cols(self):
        return self._start_cols + (self._round // 3)
    
    def get_rows(self):
        return self._start_rows
    
    def get_ball_vel(self):
        return self._start_ball_vel + (self._round * self._ball_vel_incr)
    
    def get_platform_vel(self):
        return self._start_platform_vel + ((self._round // 2) * self._platform_vel_incr)

    def get_score(self):
        return self._score

    def on_won(self):
        self._round += 1
        self.refresh_bricks()
        self._scene = "game_level"
        Engine.get().set_active_scene(self._scene)


    def brick_broken(self, points : int):
        self._score += points
        self._bricks_left -= 1
        if self._bricks_left == 0:
            self.on_won()

    def get_leaderboard(self):
        return self._db.get_scores()
    
    def get_players_best(self):
        return self._db.get_player_score(self._player)
