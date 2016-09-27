from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.listview import ListView
from peewee_db import User, Book
from kivy.uix.floatlayout import FloatLayout


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        box_layout = BoxLayout(orientation='vertical')
        box_layout.add_widget(Label(text="----User: %s----" % '0000',))

        books = ["<<%s>>  |  borrowed by:  %s" % (
            book.name, book.user.name) if book.user is not None else "<<%s>>  |  not borrowed" % book.name for book in
                 Book.select()]

        for word in books:
            btn = Button(text=word, size=(10, 5))
            btn.bind(on_press=self.pop)
            box_layout.add_widget(btn)

        self.add_widget(box_layout)

    def pop(self, *args):
        btn = Button(text='borrow/return ?')
        popup = Popup(title='Test popup', content=btn, auto_dismiss=False, size_hint=(0.5, 0.2))
        btn.bind(on_press=popup.dismiss)

        popup.open()


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()