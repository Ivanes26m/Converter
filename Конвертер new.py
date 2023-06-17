from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Window.size = (1000, 500)
Window.clearcolor = (200/255, 100/255, 30/255, 1)
Window.title = 'Конвертер'

# Стартовая страница
class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертер')
        self.miles = TextInput(hint_text='Введите значение (мили)', multiline=False)
        self.metres = TextInput(hint_text='Введите значение (метры)', multiline=False)
        self.santimetres = TextInput(hint_text='Введите значение (сантиметры)', multiline=False)
        self.kilometres = TextInput(hint_text='Введите значение (километры)', multiline=False)
        self.btn1 = Button(text="Сброс", on_press=self.press_btn)

        self.miles.bind(text=self.on_text)
        self.metres.bind(text=self.on_text)
        self.santimetres.bind(text=self.on_text)
        self.kilometres.bind(text=self.on_text)

    def press_btn(self, *args):
        self.kilometres.text = ''
        self.santimetres.text = ''
        self.metres.text = ''
        self.miles.text = ''

        self.kilometres.text = ''
        self.santimetres.text = ''
        self.metres.text = ''
        self.miles.text = ''

    def on_text(self, *args):
        if self.kilometres.text.isnumeric():
            data = self.kilometres.text
            self.miles.text = 'Мили: ' + str(float(data) * 0.62)
            self.metres.text = 'Метры: ' + str(float(data) * 1000)
            self.santimetres.text = 'Сантиметры: ' + str(float(data) * 10000)

        if self.miles.text.isnumeric():
            data = self.miles.text
            self.kilometres.text = 'Километры: ' + str(float(data) / 0.62)
            self.metres.text = 'Метры: ' + str(float(data) / 0.62 * 1000)
            self.santimetres.text = 'Сантиметры: ' + str(float(data) / 0.62 * 10000)

        if self.metres.text.isnumeric():
            data = self.metres.text
            self.kilometres.text = 'Километры: ' + str(float(data) / 1000)
            self.miles.text = 'Мили: ' + str(float(data) / 0.62 / 1000)
            self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100)

        if self.santimetres.text.isnumeric():
            data = self.santimetres.text
            self.kilometres.text = 'Километры: ' + str(float(data) / 10000)
            self.metres.text = 'Метры: ' + str(float(data) / 100)
            self.miles.text = 'Мили: ' + str(float(data) / 0.62 / 10000)

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.santimetres)
        box.add_widget(self.kilometres)
        box.add_widget(self.btn1)
        return box

if __name__ == '__main__':
    MyApp().run()
