# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import ListView
from peewee_db import User, Book

# store global data between screens:
global_data = {}


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name_input = TextInput(text='put your name.')
        self.pass_input = TextInput(text='put your password.')

        box_layout = BoxLayout(orientation='vertical')
        title_label = Label(text="----Main page----", font_size='24dp')

        name_layout = BoxLayout(padding=[30, 30, 30, 30])
        name_layout.add_widget(Label(text="username"))
        name_layout.add_widget(self.name_input)
        passwd_layout = BoxLayout(padding=[30, 30, 30, 30])
        passwd_layout.add_widget(Label(text="password"))
        passwd_layout.add_widget(self.pass_input)

        login_button = Button(text="Login in")
        login_button.bind(on_press=self.login)

        sign_button = Button(text="Sign in ")
        sign_button.bind(on_press=self.sign)

        box_layout.add_widget(title_label)
        box_layout.add_widget(name_layout)
        box_layout.add_widget(passwd_layout)
        box_layout.add_widget(login_button)
        box_layout.add_widget(sign_button)
        self.add_widget(box_layout)

    def login(self, *args):
        try:
            User.get(User.name == self.name_input.text, User.password == self.pass_input.text)
            global_data['user_name'] = self.name_input.text
            self.manager.add_widget(BookScreen(name='book'))
            self.manager.current = 'book'
        except Exception:
            self.name_input.text = self.pass_input.text = 'name or password not right'

    def sign(self, *args):
        self.manager.add_widget(SignScreen(name='sign'))
        self.manager.current = 'sign'


class SignScreen(Screen):
    def __init__(self, **kwargs):
        super(SignScreen, self).__init__(**kwargs)
        self.name_input = TextInput(text='put your name.')
        self.pass_input = TextInput(text='put your password.')

        box_layout = BoxLayout(orientation='vertical')
        title_label = Label(text="----Sign page----", font_size='24dp')

        name_layout = BoxLayout(padding=[30, 30, 30, 30])
        name_layout.add_widget(Label(text="username"))
        name_layout.add_widget(self.name_input)
        passwd_layout = BoxLayout(padding=[30, 30, 30, 30])
        passwd_layout.add_widget(Label(text="password"))
        passwd_layout.add_widget(self.pass_input)

        sign_button = Button(text="Sign in ")
        sign_button.bind(on_press=self.sign)

        box_layout.add_widget(title_label)
        box_layout.add_widget(name_layout)
        box_layout.add_widget(passwd_layout)
        box_layout.add_widget(sign_button)
        self.add_widget(box_layout)

    def sign(self, *args):
        User.get_or_create(name=self.name_input.text, password=self.pass_input.text)
        self.manager.current = 'main'


class BookScreen(Screen):
    def __init__(self, **kwargs):
        super(BookScreen, self).__init__(**kwargs)
        total_layout = BoxLayout()

        box_layput = BoxLayout()
        box_layput.add_widget(Label(text="----Book list----"))
        user_button = Button(text='User Setting')
        user_button.bind(on_press=self.setting)
        box_layput.add_widget(user_button)

        books = ["<<%s>>  |  borrowed by:  %s" % (
            book.name, book.user.name) if book.user is not None else "<<%s>>  |  not borrowed" % book.name for book in
                 Book.select()]

        adapter = SimpleListAdapter(data=books, cls=Button)
        list_view = ListView(adapter=adapter)

        total_layout.add_widget(box_layput)
        total_layout.add_widget(list_view)
        self.add_widget(total_layout)

    def setting(self, *args):
        self.manager.add_widget(UserScreen(name='user'))
        self.manager.current = 'user'


class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)

        box_layout = BoxLayout()
        title_label = Label(name='----User: %s----' % global_data['user_name'])

        book_list = [book.name for book in User.get(User.name == global_data['user_name']).books]
        list_view = ListView(item_strings=book_list)

        box_layout.add_widget(title_label)
        box_layout.add_widget(list_view)
        self.add_widget(box_layout)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()
