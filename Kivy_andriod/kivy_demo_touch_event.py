from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# [layout + wiget]   +   [event callback]

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='1'))

        bt = Button(text='---->')
        bt.bind(on_touch_down=self.btn_pressed)  # touch event's callback
        self.add_widget(bt)

        self.add_widget(Button(text='2'))

    def btn_pressed(self, *args):  # main eventloop will pass multi parameters to this callbak
        print args
        print '---->here in touch event callback---->'


class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
