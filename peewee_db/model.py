from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('sqlite.db')


# define model:
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(unique=True)
    password = CharField()


class Book(BaseModel):
    name = CharField(unique=True)
    user = ForeignKeyField(User, related_name='books')  # None if is_borrowed = False
    is_borrowed = BooleanField(default=False)


# set up db tables:
db.connect()
db.create_tables([User, Book])
