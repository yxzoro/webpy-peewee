from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('sqlite.db')


# define model:
class BaseModel(Model):
    class Meta:
        database = db

    @staticmethod
    def get(cls, *query, **kwargs):
        try:
            return cls.get(*query, **kwargs)
        except Exception:  # doesn't exist
            return None


class User(BaseModel):
    name = CharField(unique=True)
    password = CharField()


class Book(BaseModel):
    name = CharField(unique=True)
    user = ForeignKeyField(User, related_name='books')  # None if is_borrowed = False
    is_borrowed = BooleanField(default=False)


