from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='test-1'))
        self.add_widget(Button(text='btn 1'))

        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)  # pressed event callback
        self.add_widget(cb)

        self.add_widget(Button(text='btn 2'))
        self.add_widget(Button(text='test-2'))

    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])  # add a property: pressed -> can raise property event later when value changed.

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    # ----------------------------------https://kivy.org/docs/guide/events.html------------------------------ #
    # ------------------------------------------on_XX() method handle touch event --------------------------- #

    def on_pressed(self, instance, pos):
        print ('pressed at {pos}'.format(pos=pos))


# ------------------------------------------------------------------------------------------------------- #

class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
