import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


class DummyApp(App):
    def build(self):
        self.formula = '0'

        bL = BoxLayout(orientation='vertical', padding=10)
        gL = GridLayout(cols=4, spacing=2, size_hint=(1, .6))
        self.lbl = Label(text='0', font_size=100, size_hint=(1, .4))
        bL.add_widget(self.lbl)
        for i in range(3):
            gL.add_widget(Widget())
        gL.add_widget(Button(text='/', on_press=self.add_operation))

        gL.add_widget(Button(text='7', on_press=self.add_number))
        gL.add_widget(Button(text='8', on_press=self.add_number))
        gL.add_widget(Button(text='9', on_press=self.add_number))
        gL.add_widget(Button(text='*', on_press=self.add_operation))

        gL.add_widget(Button(text='4', on_press=self.add_number))
        gL.add_widget(Button(text='5', on_press=self.add_number))
        gL.add_widget(Button(text='6', on_press=self.add_number))
        gL.add_widget(Button(text='-', on_press=self.add_operation))

        gL.add_widget(Button(text='1', on_press=self.add_number))
        gL.add_widget(Button(text='2', on_press=self.add_number))
        gL.add_widget(Button(text='3', on_press=self.add_number))
        gL.add_widget(Button(text='+', on_press=self.add_operation))

        gL.add_widget(Button(text='C', on_press=self.cancel))
        gL.add_widget(Button(text='0', on_press=self.add_number))
        gL.add_widget(Button(text='.', on_press=self.add_number))
        gL.add_widget(Button(text='=', on_press=self.calc_result))

        bL.add_widget(gL)

        return bL

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def update_label(self):
        self.lbl.text = self.formula

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = self.lbl.text

    def cancel(self, instance):
        self.formula = '0'
        self.update_label()


if __name__ == ('__main__'):
    DummyApp().run()
