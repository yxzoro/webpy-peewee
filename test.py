# -*- coding: utf-8 -*-

from peewee_db.model import User, Book

# User.create(name='d', password='s')

print ["%s, borrowed by: %s" % (book.name, book.user.name) if book.user is not None else "%s, not borrowed" % book.name for book in Book.select()]




