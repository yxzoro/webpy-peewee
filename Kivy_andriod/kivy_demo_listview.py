from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.adapters.simplelistadapter import SimpleListAdapter


class MainView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(MainView, self).__init__(**kwargs)



        simple_list_adapter = SimpleListAdapter(data=["book name: {0}".format(i) for i in range(10)], cls=Button)
        list_view = ListView(adapter=simple_list_adapter)
        self.add_widget(list_view)

if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MainView(width=800))
