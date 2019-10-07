from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config
import random                                       

Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '40')

class Measure():                                   
    def temp_module(self):
        return(round(random.random()*40,1))         

class Display(Widget):
    def on_measure(self):                           
        temp=Measure()
        self.ids.la01.text=str(temp.temp_module())

class TestApp(App):
    def build(self):
        disp=Display()
        return disp

if __name__ == '__main__':
    TestApp().run()