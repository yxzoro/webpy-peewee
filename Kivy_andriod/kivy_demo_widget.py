from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

'''
# kivy Andriod app develop key points:

1. draw UI = layout + widget 
2. handle touch event of a widget = on_touch() callback
'''


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)  # object-oriented, add multi [widgets] to root [Layout].
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return LoginScreen()  # return root Layout 


if __name__ == '__main__':
    MyApp().run()
