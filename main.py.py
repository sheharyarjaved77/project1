# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config

# Set window size
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.result_text = TextInput(text='', multiline=False, readonly=True, font_size=40, halign='right')
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '1', '=', '+'],
            ['C']
        ]

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result_text)

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.result_text.text = str(eval(self.expression))
                self.expression = self.result_text.text
            except Exception as e:
                self.result_text.text = "Error"
                self.expression = ""
        elif instance.text == 'C':
            self.expression = ""
            self.result_text.text = ""
        else:
            self.expression += instance.text
            self.result_text.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
