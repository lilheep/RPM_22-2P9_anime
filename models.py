from peewee import SqliteDatabase, Model, TimeField, IntegerField, TextField, ForeignKeyField, DateTimeField, CharField
 
db = SqliteDatabase('sqlite.db') 
 
class DB(Model): 
 
    class Meta: 
        database = db 
 
class User(DB): 
    tg_user = IntegerField(primary_key=True)
    time = TimeField(null=True)
class Genres(DB):
    Genre = CharField(null=True)

class Years(DB):
    Year = CharField(null=True)

class Photo(DB):
    PhotoUrl = TextField(null=True)
class Anime(DB):
    Anime = TextField(null=True)
    Link = TextField(null=True)
    Genre = ForeignKeyField(Genres, backref='animes', null=True)
    Years = ForeignKeyField(Years, backref='animes', null=True)
    PhotoUrl = ForeignKeyField(Photo, backref='animes', null=True)

class SentAnime(DB):
    user = ForeignKeyField(User, backref='sent_anime')
    anime = ForeignKeyField(Anime, backref='sent_to_users')


db.connect() 
db.create_tables([User,Anime,Genres,Years,Photo,SentAnime],  safe=True) 
db.close()