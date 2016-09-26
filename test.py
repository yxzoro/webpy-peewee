from peewee_db.model import User, Book

# User.create(name='d', password='s')

print User.get(User.name == 'test')




