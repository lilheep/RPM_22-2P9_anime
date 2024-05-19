"""Создание базы данных"""
from peewee import SqliteDatabase, Model, TextField, ForeignKeyField
db = SqliteDatabase('sqlite.db')
class Datebase(Model):
    """Создание таблицы"""
    class Meta:
        """Класс мета"""
        database = db
class Genres(Datebase):
    """Создание таблицы с жанрами"""
    Genre = TextField()
    
class Anime(Datebase):
    """Создание таблицы с аниме"""
    Anime = TextField()
    Link = TextField()
    Genre = ForeignKeyField(Genres)


class Test(Datebase):
    """Информация по аниме"""
    Type = TextField()
    Episodes = TextField()
    Status = TextField()
    Genre = TextField()
    Origin = TextField()
    Agelimit = TextField()
    Studio = TextField()
    Voiceover = TextField()

db.connect()
db.create_tables([Genres,Anime,Test], safe=True)
db.close()
