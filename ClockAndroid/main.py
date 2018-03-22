from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time

Window.clearcolor = get_color_from_hex('#abcdef')
LabelBase.register(name='Roboto', fn_regular='Roboto-Thin.ttf', fn_bold='Roboto-Medium.ttf')


class ClockLayout(BoxLayout):
    pass


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def build(self):
        self.root.ids.start_stop.background_normal, self.root.ids.start_stop.background_down = 'down.png', 'normal.png'
        self.root.ids.reset.background_normal, self.root.ids.reset.background_down = 'down.png', 'normal.png'
    def update_time(self, nap):
        self.root.ids.time.text = time.strftime('[b]%H[/b]:%M:%S')
        # self.root.time_prop.text = 'demo'

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)
            self.root.ids.stopwatch.text = (
                '%02d:%02d.[size=200]%02d[/size]' % (int(minutes), int(seconds), int(seconds * 100 % 100)))

    def start_stop(self):
        if not self.sw_started:
            # self.root.ids.start_stop.text = ('Start' if self.sw_started else "Stop")
            self.root.ids.start_stop.text = 'Stop'
            self.sw_started = True
        else:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0
        self.root.ids.stopwatch.text = '00:00.[size=200]00[/size]'


if __name__ == '__main__':
    ClockApp().run()
