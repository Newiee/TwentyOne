from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class TwentyOneApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


TwentyOneApp().run()



