# ---------------------------------------http://webpy.org/------------------------------------------ #

import web
import json
from peewee_db.model import User, Book

urls = (
    '/test', 'MyTest',
    '/login', 'Login',
    '/sign', 'Sign',
    '/books', 'Books',
    '/update_book', 'Update_Book',
)


# web.input() == a dict(), you can get data from it.
class MyTest:
    def GET(self):
        print web.input()
        return json.dumps({"hello": 'get'})

    def POST(self):
        print web.input()
        return json.dumps({"hello": 'post'})


class Login:
    def POST(self):
        data = web.input()
        try:
            User.get(User.name == data['name'], User.password == data['passwd'])
            flag = 'success'
        except Exception:
            flag = 'fail'
        return json.dumps({"flag": flag})


class Sign:
    def POST(self):
        data = web.input()
        User.get_or_create(name=data['name'], password=data['passwd'])


class Books:
    def POST(self):
        books = ["<<%s>>  |  borrowed by:  %s" % (
            book.name, book.user.name) if book.user is not None else "<<%s>>  |  not borrowed" % book.name for book in
                 Book.select()]
        return json.dumps({"books": books})


class Update_Book:
    def POST(self):
        data = web.input()
        if 'user_name' in data.keys():
            Book.update(user=User.get(name=data['user_name'])).where(Book.name == data['book_name']).execute()
        else:
            Book.update(user=None, is_borrowed=False).where(Book.name == data['book_name']).execute()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


# get response json:
# import requests
# data = requests.get(url='http://localhost:8080/test')
# print data.content
