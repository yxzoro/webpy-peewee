from model import *

# create db tables:
db.connect()
db.create_tables([User, Book])

