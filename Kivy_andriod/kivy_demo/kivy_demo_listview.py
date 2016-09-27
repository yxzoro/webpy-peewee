from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.listview import ListView
from kivy.adapters.simplelistadapter import SimpleListAdapter


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        title = ['----Book page----']
        books = ["book name: {0}".format(i) for i in range(30)]

        simple_list_adapter = SimpleListAdapter(data=title + books, cls=Button)
        print simple_list_adapter
        list_view = ListView(adapter=simple_list_adapter)

        self.add_widget(list_view)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()