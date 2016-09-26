from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from peewee_db import User, Book


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name_input = TextInput(text='put your name.')
        self.pass_input = TextInput(text='put your password.')

        box_layout = BoxLayout(orientation='vertical')
        title_label = Label(text="Main page", font_size='24dp')

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
        if User.get(User.name == self.name_input.text, User.password == self.pass_input.text):
            self.manager.current = 'book'
        else:
            self.name_input.text = self.pass_input.text = 'name or password not right'

    def sign(self, *args):
        self.manager.current = 'sign'


class SignScreen(Screen):
    def __init__(self, **kwargs):
        super(SignScreen, self).__init__(**kwargs)
        self.name_input = TextInput(text='put your name.')
        self.pass_input = TextInput(text='put your password.')

        box_layout = BoxLayout(orientation='vertical')
        title_label = Label(text="Main page", font_size='24dp')

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
        if User.get(User.name == self.name_input.text):
            pass
        else:
            User.create(name=self.name_input.text, password=self.pass_input.text)
        self.manager.current = 'main'


class BookScreen(Screen):
    def __init__(self, **kwargs):
        super(BookScreen, self).__init__(**kwargs)

        box_layput = BoxLayout(orientation='vertical')
        title_label = Label(text="----Book page----")

        box_layput.add_widget(title_label)
        self.add_widget(box_layput)


class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)

        my_box1 = BoxLayout(orientation='vertical')
        my_label1 = Label(text="User page")

        self.add_widget(my_box1)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(SignScreen(name='sign'))
        screen_manager.add_widget(BookScreen(name='book'))
        screen_manager.add_widget(UserScreen(name='user'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()
