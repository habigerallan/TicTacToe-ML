import kivy
kivy.require('2.2.1')

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '360')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.graphics import Rectangle

class TTTSquare(Button):
    def __init__(self, index, **kwargs):
        super(TTTSquare, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (1, 1, 1, 1)
        self.index = index

class TTTBoard(GridLayout):
    def __init__(self, **kwargs):
        super(TTTBoard, self).__init__(**kwargs)
        self.padding = 0
        self.spacing = 25
        self.cols = 3
        self.rows = 3

        with self.canvas.before:
            Color(0, 0, 0, 1)  # Set the canvas color to black
            self.rect = Rectangle(pos=self.pos, size=self.size)

        for i in range(9):
            square = TTTSquare(index=i)
            self.add_widget(square)
    def on_size(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

            

class GameDisplay(BoxLayout):
    def __init__(self, **kwargs):
        super(GameDisplay, self).__init__(**kwargs)
        self.size_hint_x = 2/3
        self.size_hint_y = 1
        self.orientation = 'horizontal'  # Change to horizontal orientation
        self.board = TTTBoard()
        self.add_widget(self.board)


class TicTacToeApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return GameDisplay()

if __name__ == '__main__':
    TicTacToeApp().run()