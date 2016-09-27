# encoding=utf-8
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from peewee_db import User, Book
from webpy.server_adapter import adapter

# store data between screens:
global_data = {}


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name_input = TextInput(text='put your name.', size_hint=(0.8, 1))
        self.pass_input = TextInput(text='put your password.', size_hint=(0.8, 1))

        box_layout = BoxLayout(orientation='vertical')
        title_label = Label(text="----Main page----", size_hint=(1, 0.15))

        name_layout = BoxLayout(padding=[10, 10, 10, 10], spacing=20, orientation='horizontal', size_hint=(1, 0.25))
        name_layout.add_widget(Label(text="username", size_hint=(0.2, 1)))
        name_layout.add_widget(self.name_input)
        passwd_layout = BoxLayout(padding=[10, 10, 10, 10], spacing=20, orientation='horizontal', size_hint=(1, 0.25))
        passwd_layout.add_widget(Label(text="password", size_hint=(0.2, 1)))
        passwd_layout.add_widget(self.pass_input)

        login_button = Button(text="Login in", size_hint=(1, 0.2))
        login_button.bind(on_press=self.login)

        sign_button = Button(text="Sign in ", size_hint=(1, 0.2))
        sign_button.bind(on_press=self.sign)

        box_layout.add_widget(title_label)
        box_layout.add_widget(name_layout)
        box_layout.add_widget(passwd_layout)
        box_layout.add_widget(login_button)
        box_layout.add_widget(sign_button)
        self.add_widget(box_layout)

    def login(self, *args):
        flag = adapter.login(name=self.name_input.text, passwd=self.pass_input.text)['flag']
        if flag == 'success':
            global_data['user_name'] = self.name_input.text
            self.manager.add_widget(BookScreen(name='book'))
            self.manager.current = 'book'
        else:
            self.name_input.text = self.pass_input.text = 'name or password not right'

    def sign(self, *args):
        self.manager.add_widget(SignScreen(name='sign'))
        self.manager.current = 'sign'


class SignScreen(Screen):
    def __init__(self, **kwargs):
        super(SignScreen, self).__init__(**kwargs)

        self.name_input = TextInput(text='put your name.', size_hint=(0.8, 1))
        self.pass_input = TextInput(text='put your password.', size_hint=(0.8, 1))

        box_layout = BoxLayout(orientation='vertical')
        title_label = Label(text="----Sign page----", size_hint=(1, 0.15))

        name_layout = BoxLayout(padding=[10, 10, 10, 10], spacing=20, orientation='horizontal', size_hint=(1, 0.25))
        name_layout.add_widget(Label(text="username", size_hint=(0.2, 1)))
        name_layout.add_widget(self.name_input)
        passwd_layout = BoxLayout(padding=[10, 10, 10, 10], spacing=20, orientation='horizontal', size_hint=(1, 0.25))
        passwd_layout.add_widget(Label(text="password", size_hint=(0.2, 1)))
        passwd_layout.add_widget(self.pass_input)

        sign_button = Button(text="Sign in ", size_hint=(1, 0.2))
        sign_button.bind(on_press=self.sign)

        box_layout.add_widget(title_label)
        box_layout.add_widget(name_layout)
        box_layout.add_widget(passwd_layout)
        box_layout.add_widget(sign_button)
        self.add_widget(box_layout)

    def sign(self, *args):
        adapter.sign(name=self.name_input.text, passwd=self.pass_input.text)
        self.manager.current = 'main'


class BookScreen(Screen):
    def __init__(self, **kwargs):
        super(BookScreen, self).__init__(**kwargs)
        box_layout = BoxLayout(orientation='vertical')
        box_layout.add_widget(Label(text="----User: %s----" % global_data['user_name'], size_hint=(1, 0.1)))

        books = adapter.books()['books']
        for word in books:
            btn = Button(text=word, size_hint=(1, 0.05))
            btn.bind(on_press=self.pop)
            box_layout.add_widget(btn)
        self.add_widget(box_layout)

    def pop(self, *args):
        button_text = args[0].text
        book_name = button_text.split(' | ')[0]
        global_data.update({'book_name': book_name})
        if 'borrowed by' in button_text:
            if global_data['user_name'] in button_text:
                text = 'return %s ?' % book_name
            else:
                text = '%s is already borrowed...' % book_name
        else:
            text = 'borrow %s ?' % book_name
        btn = Button(text='ok')
        popup = Popup(title=text, content=btn, size_hint=(0.5, 0.2))
        global_data['pop'] = popup
        btn.bind(on_press=self.dismiss)
        popup.open()

    def dismiss(self, *args):
        popup = global_data['pop']
        popup.dismiss()
        book_name = global_data['book_name'][2:-3]
        if 'return' in popup.title:
            adapter.update_book(book_name=book_name)
        elif 'borrowed' not in popup.title:
            adapter.update_book(user_name=global_data['user_name'], book_name=book_name)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()
