from peewee import SqliteDatabase, Model, TimeField, IntegerField
 
db = SqliteDatabase('sqlite.db') 
 
class DB(Model): 
 
    class Meta: 
        database = db 
 
class User(DB): 
    tg_user = IntegerField(primary_key=True)
    time = TimeField(null=True)
 
db.connect() 
db.create_tables([User],  safe=True) 
db.close()