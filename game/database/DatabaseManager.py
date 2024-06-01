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
   
    def set_player_score(self, player: Player, score_val: int):
        try:
            score = Score.get(Score.player == player)
            score.score = score_val
            score.save()
        except Score.DoesNotExist:
            Score.create(player=player, score=score_val)

    def get_num_players(self):
        return Player.select().count()
    
    def get_scores(self, num : int):
        return list(Score.select().order_by(Score.score.desc()).limit(num))
        
    def get_worst_score(self):
        return Score.select().order_by(Score.score.asc()).limit(1).get()
    
    def delete_player(self, player: Player):
        Score.delete().where(Score.player == player).execute()
        player.delete_instance()
        