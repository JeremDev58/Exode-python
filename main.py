from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty
from kivy.uix.button import Button

AnchorLayout
Builder.load_file('main.kv')

class Codex(App):
    def build(self):
        return BLMain()

class BtnRound(Button):
    def __init__(self, **kwargs):
        super(BtnRound, self).__init__(**kwargs)


class BLMain(BoxLayout):
    def __init__(self, **kwargs):
        super(BLMain, self).__init__(**kwargs)
        


class BLTop(FloatLayout):
    def __init__(self, **kwargs):
        super(BLTop, self).__init__(**kwargs)
        self.add_widget(BLTopMenu())


class BLScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(BLScreen, self).__init__(**kwargs)
        self.add_widget(BLSideMenu())
        self.add_widget(Views())


class BLTopMenu(AnchorLayout):
    def __init__(self, **kwargs):
        super(BLTopMenu, self).__init__(**kwargs)
        self.anchor_x= 'right' 
        self.anchor_y='bottom'


class BLSideMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(BLSideMenu, self).__init__(**kwargs)


class Views(Widget):
    def __init__(self, **kwargs):
        super(Views, self).__init__(**kwargs)

        
if __name__ == '__main__':
    Codex().run()

