from .Model import Player, Score
from peewee import SqliteDatabase

class DatabaseManager:
    
    def __init__(self):
        self._db = None

    def load(self, db_name):
        path = "game\\database\\" + db_name + ".db"
        database = SqliteDatabase(path)
        Player._meta.database = database
        Score._meta.database = database
        database.connect()
        database.create_tables([Player, Score])
        self._db = database

    def get_all_players(self):
        return Player.select()
    
    def get_player_score(self, player: Player):
        score = Score.select().where(Score.player == player)
        if len(score) == 0:
            return 0
        return score[0].score
   
    def set_player_score(self, player: Player, score: int):
        try:
            score = Score.get(Score.player == player)
            score.score = score
            score.save()
        except Score.DoesNotExist:
            Score.create(player=player, score=score)

    def get_num_players(self):
        return Player.select().count()
    
    def remove_excess(self, threshold : int):
        num = Score.select().count()
        while num > threshold:
            worst = self.get_worst_score()
            worst.delete_instance()
            num -= 1
        

    def get_worst_score(self):
        return Score.select().order_by(Score.score.asc()).limit(1)