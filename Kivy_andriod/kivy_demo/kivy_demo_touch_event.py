from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
import requests


# ----------------------------------- [layout + widget]  +  [event callback]--------------------------------- #


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.add_widget(Button(text='book1'))
        bt = Button(text='---->')
        bt.bind(on_press=self.btn_pressed)  # touch event's callback
        self.add_widget(bt)

        self.add_widget(Button(text='book2'))

    def btn_pressed(self, *args):

        pass


class MyLayout2(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout2, self).__init__(**kwargs)

        bt = Button(text='-->back-->')
        bt.bind(on_touch_down=self.btn_pressed)
        self.add_widget(bt)

    def btn_pressed(self, *args):
        self.root.manager.current = 'screen1'
        pass


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen1 = Screen(name='screen1')
        screen1.add_widget(MyLayout(orientation='vertical'))
        screen2 = Screen(name='screen2')
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)
        return screen_manager


if __name__ == '__main__':
    MyApp().run()
