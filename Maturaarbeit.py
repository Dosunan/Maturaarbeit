import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window



#Define our different screens
class FirstWindow(Screen):
    pass
class MondayWindow(Screen):
    pass
class TuesdayWindow(Screen):
    pass
class WednesdayWindow(Screen):
    pass
class ThursdayWindow(Screen):
    pass
class FridayWindow(Screen):
    pass
class SaturdayWindow(Screen):
    pass
class SundayWindow(Screen):
    pass


class WindowManager (ScreenManager):
    pass
kv = Builder.load_file('menuplan.kv')
 
        
class Menuplan(App):
    
    def build(self):
        return kv

class WindowManager(App):
    def build(self):
        return Button



    
if __name__ == "__main__":
    Menuplan().run()
