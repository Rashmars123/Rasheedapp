from datetime import time

from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import *
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

Builder.load_file("mainapp.kv")


class LoginScreen(Screen):

    def tomainscreen(self):
        self.manager.current = "Main_screen"


class MainScreen(Screen):

    def toMain(self):
        self.manager.current = "Login_screen"
        self.transition_state = "out"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
