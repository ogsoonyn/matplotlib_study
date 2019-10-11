# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.config import Config

import mychart

import concurrent.futures
import threading

# ゴリ押しで設定値をTestAppにわたすためのデータ保持クラス
class SignletonMyChart(mychart.MyChart):
    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton == None:
            cls.__singleton = super(SignletonMyChart, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

class TextWidget(Widget):
    #text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        #self.text = ''

    #def buttonClicked(self):
        #self.text = 'hogehoge'

    def _on_clicked(self):
        chart = SignletonMyChart()
        chart.type_string = self.get_radiobutton_status()
        chart.invert_xaxis = self.ids.cb_invert_x.active
        chart.invert_yaxis = self.ids.cb_invert_y.active
        chart.change_color_per_stroke = self.ids.cb_color_per_stroke.active
        chart.xy_swap = self.ids.cb_xy_swap.active

    def get_radiobutton_status(self):
        if self.ids.gtype_line.active:
            return "line"
        elif self.ids.gtype_ox.active:
            return "circlecross"
        elif self.ids.gtype_plus.active:
            return "pluscross"
        elif self.ids.gtype_period.active:
            return "period"
        else:
            return "default"

    def show_previous_chart(self):
        chart = SignletonMyChart()
        chart.showChart()

class TestApp(App):
    #executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = "csv2chart"
        self._file = Window.bind(on_dropfile = self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        #self.executor.submit(mychart.showChart(file_path.decode('utf-8')))
        #thread = threading.Thread(target = mychart.showChart(file_path.decode('utf-8')))
        #thread.start()

        #typ = self.widget.ids.g0.active ? "line" : "point"
        #typ = "line" if self.widget.ids.g0.active else "point"

        chart = SignletonMyChart()
        chart.source_file_name = file_path.decode('utf-8')
        chart.chart_title = file_path.decode('utf-8')
        chart.showChart()
        #mychart.showChart2(file_path.decode('utf-8'), typ)
        #print(file_path.decode('utf-8'))
        #thread.join()
        return

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    TestApp().run()
