from peewee import Model, CharField, IntegerField, AutoField, ForeignKeyField

class Player(Model):
    uid = AutoField()
    name = CharField(unique=True)
    password = CharField()

class Score(Model):
    player = ForeignKeyField(Player, backref='scores', primary_key=True)
    score = IntegerField()