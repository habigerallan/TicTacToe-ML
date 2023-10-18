import kivy
kivy.require('2.2.1')

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle, Line, Ellipse

class TicTacToeApp(App):
    def __init__(self):
        self.game_layout = GameLayout()

    def build(self):
        Window.size = (640, 360)

        root = Root()
        root_bg = Background(color=(1,1,1,1), parent=root)
        root.add_widget(root_bg)

        game_frame = GameFrame()
        game_frame_bg = Background(color=(0,0,0,.1), parent=game_frame)
        game_frame.add_widget(game_frame_bg)
        root.add_widget(game_frame)

        game_frame.add_widget(self.game_layout)
        return root

class Root(RelativeLayout):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.size = Window.size
        self.pos = (0,0)

class GameFrame(RelativeLayout):
    def __init__(self, **kwargs):
        super(GameFrame, self).__init__(**kwargs)
        self.size_hint_x = 360 / 640
        self.size_hint_y = 1

class GameLayout(GridLayout):
    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        self.padding = 25
        self.spacing = 25
        self.cols = 3
        self.rows = 3
        self.cells = []

        for i in range(9):
            cell = GameCell(index=i)
            self.add_widget(cell)
            self.cells.append(cell)

    def clear_cells(self):
        for cell in self.cells:
            cell.canvas.clear()
            self.remove_widget(cell)

        self.cells = []            
        for i in range(9):
            cell = GameCell(index=i)
            self.add_widget(cell)
            cell.parent = self
            self.cells.append(cell)
        
class GameCell(Button):
    def __init__(self, index, **kwargs):
        super(GameCell, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (1, 1, 1, 1)
        self.index = index        
        self.selected = False
        self.filled = False

        self.bind(on_press=self.mouse1_down)

    def mouse1_down(self, cell):
        if not cell.filled:
            cell.selected = True

    def draw_x(self):
        with self.canvas.after:
            Color(0, 0, 0, 1)
            Line(points=[self.x, self.y, self.right, self.top], width=10)
            Line(points=[self.x, self.top, self.right, self.y], width=10)


    def draw_o(self):
        with self.canvas.after:
            Color(1, 1, 1, 1)
            Ellipse(pos=self.pos, size=self.size)
            Color(0, 0, 0, 1)
            Line(circle=[self.center_x, self.center_y, min(self.width, self.height) / 2], width=10)

class Background(Widget):
    def __init__(self, color, parent, **kwargs):
        super(Background, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(pos=parent.pos, size=parent.size)

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    