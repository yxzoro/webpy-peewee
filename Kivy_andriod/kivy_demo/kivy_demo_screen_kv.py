from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<LoginScreen>:
    BoxLayout:
        orientation:'vertical'
        Button:
            text: 'Goto settings'
            on_press: root.manager
            text: 'Quit'

<BookScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<UserScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")


# Declare screens
class LoginScreen(Screen):

    pass


class BookScreen(Screen):
    pass


class UserScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(BookScreen(name='book'))
sm.add_widget(UserScreen(name='user'))


class MyApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
