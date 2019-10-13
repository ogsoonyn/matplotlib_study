from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
import random                                       

Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '150')

class Measure():                                   
    def temp_module(self):
        return(round(random.random()*40,1))         

class Display(Widget):
    def on_measure(self):                           
        temp=Measure()
        if self.ids.g0.active:                              
            self.ids.l0.text=str(temp.temp_module()) + '\'C' 
        else:
            self.ids.l0.text='xx\'C' 
 
        if self.ids.g1.active:                              
            self.ids.l1.text=str(temp.temp_module()) + '\'C'  
        else:
            self.ids.l1.text='xx\'C' 
 
        if self.ids.g2.active:                              
            self.ids.l2.text=str(temp.temp_module()) + '\'C'  
        else:
            self.ids.l2.text='xx\'C' 
 

class Test2App(App):
    def build(self):
        disp=Display()
        return disp

if __name__ == '__main__':
    Test2App().run()