from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.core.window import Window

import mychart

import concurrent.futures
import threading

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        self.text = 'hogehoge'

class TestApp(App):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = "csv2chart"

        self._file = Window.bind(on_dropfile = self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        #self.executor.submit(mychart.showChart(file_path.decode('utf-8')))
        #thread = threading.Thread(target = mychart.showChart(file_path.decode('utf-8')))
        #thread.start()
        mychart.showChart2(file_path.decode('utf-8'))
        print(file_path.decode('utf-8'))
        #thread.join()
        return

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    TestApp().run()
