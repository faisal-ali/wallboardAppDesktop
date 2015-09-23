from kivy.app import App
from kivy.core.text import LabelBase
from kivy.clock import Clock
from time import strftime
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class ClockApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)
        req = UrlRequest(
            'http://api.openweathermap.org/data/2.5/weather?q=Paris,fr',
            self.got_weather)

    def got_weather(self, req, results):
        for key, value in results['weather'][0].items():
            self.root.ids.weather.text = str(value)
            print(key, ': ', value)

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name="Roboto",
                       fn_regular="/Users/syedfaisal/Library/Fonts/Roboto-Thin.ttf",
                       fn_bold="/Users/syedfaisal/Library/Fonts/Roboto-Medium.ttf")
    
    ClockApp().run()

