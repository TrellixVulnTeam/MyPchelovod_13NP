from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (800, 480)
Window.clearcolor = (209/255, 144/255, 84/255, 1)
Window.title = "Пчеловод"


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="Добро пожаловать!",font_size=20, pos_hint={'x':.400, 'y':.240}, color=(207/255, 106/255, 39/255, 1))

    def first_button_pressed(self, *args):
        self.label.text = "Вы вошли"

    def build(self):
        box = BoxLayout()
        first_button = Button(text="Начало работы(Кнопка)", size_hint=(.5, .25), pos_hint={'x':.400, 'top':.300}, background_color=(55/255, 196/255, 57/255, 1))
        first_button.bind(on_press=self.first_button_pressed)
        box.add_widget(self.label)
        box.add_widget(first_button)

        return box


if __name__ == "__main__":
    MyApp().run()