from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests


# [layout + wiget]   +   [event callback]

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='book1'))

        bt = Button(text='---->')
        bt.bind(on_touch_down=self.btn_pressed)  # touch event's callback
        self.add_widget(bt)

        self.add_widget(Button(text='book2'))

    def btn_pressed(self, *args):  # main eventloop will pass multi parameters to this callbak
        # data = requests.get(url='http://localhost:8080/')
        # print data
        pass


class MyApp(App):
    def build(self):
        return RootWidget(orientation='vertical')


if __name__ == '__main__':
    MyApp().run()
