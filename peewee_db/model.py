from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from os.path import dirname, realpath


db = SqliteExtDatabase('%s\sqlite.db' % dirname(realpath(__file__)))


# define model:
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(unique=True)
    password = CharField()


class Book(BaseModel):
    name = CharField(unique=True)
    user = ForeignKeyField(User, related_name='books', null=True)  # None if is_borrowed = False
    is_borrowed = BooleanField(default=False)

