from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy_garden.mapview import MapView
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


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
        mapview = MapView(zoom=12, lat=54.985303, lon=73.3911524, pos=(500,400))
        box = BoxLayout()
        first_button = Button(text="Начало работы(Кнопка)", size_hint=(.5, .25), pos_hint={'x':.400, 'top':.300})
        first_button.bind(on_press=self.first_button_pressed)
        box.add_widget(self.label)
        box.add_widget(first_button)

        people_list = ScrollView(size_hint=(1, None), size=(150, 480))
        Oleg = Label(text="Пчеловод Олег", size_hint=(.10, .100), pos=(0,0))
        people_list.add_widget(Oleg)

        return mapview,box




if __name__ == "__main__":
    MyApp().run()