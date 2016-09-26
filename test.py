# -*- coding: utf-8 -*-

from peewee_db.model import User, Book

# User.create(name='d', password='s')

for i in User.get(name='yx').books:
    print i



