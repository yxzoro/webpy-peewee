from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('sqlite.db')


# define model:
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Book(BaseModel):
    user = ForeignKeyField(User, related_name='books')
    is_borrowed = BooleanField(default=True)


# set up db tables:
db.connect()
db.create_tables([User, Book])
