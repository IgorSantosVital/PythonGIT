import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import time

kivy.require('1.9.1')

class TelaLogin(GridLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Usuário'))
        self.username = TextInput(multiline=True)
        self.add_widget(self.username)
        self.add_widget(Label(text='Senha'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return TelaLogin()


if __name__ == '__main__':
    MyApp().run()
