from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        layout1 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        layout1.add_widget(Label(text='-->', size_hint=(0.8, 1)))
        layout1.add_widget(Button(text='-->', size_hint=(0.2, 1), backgroundcolor='blue'))

        layout2 = BoxLayout(orientation='vertical')
        layout2.add_widget(Button(text='1'))
        layout2.add_widget(Button(text='2'))

        layout.add_widget(layout1)
        layout.add_widget(layout2)
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()