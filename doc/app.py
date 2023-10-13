import kivy
kivy.require('2.2.1')

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line, Ellipse

class Background(Widget):
    def __init__(self, color, **kwargs):
        super(Background, self).__init__(**kwargs)
        self.color_instruction = Color(*color)
        self.rect_instruction = Rectangle(pos=self.pos, size=self.size)
        self.canvas.before.add(self.color_instruction)
        self.canvas.before.add(self.rect_instruction)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect_instruction.pos = self.pos
        self.rect_instruction.size = self.size

class TTTSquare(Button):
    def __init__(self, index, **kwargs):
        super(TTTSquare, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (.8, .8, .8, 1)
        self.index = index        
        self.filled = False

        self.bind(on_press=self.mouse1_down)

    def mouse1_down(self, instance):
        if (not instance.filled):
            if (instance.index % 2 == 0):
                self.draw_x()
            else:
                self.draw_o()
            instance.filled = True
        else:
            print("evil move spot")
        
    def draw_x(self):
        self.canvas.after.add(Color(0, 0, 0, 1))
        self.canvas.after.add(Line(points=[self.center_x, self.center_y, self.center_x + 35, self.center_y + 35], width=13))
        self.canvas.after.add(Line(points=[self.center_x, self.center_y, self.center_x - 35, self.center_y + 35], width=13))
        self.canvas.after.add(Line(points=[self.center_x, self.center_y, self.center_x + 35, self.center_y - 35], width=13))
        self.canvas.after.add(Line(points=[self.center_x, self.center_y, self.center_x - 35, self.center_y - 35], width=13))

    def draw_o(self):
        self.canvas.after.add(Color(0, 0, 0, 1))
        self.canvas.after.add(Ellipse(
            pos=(self.center_x - 50, self.center_y - 50),  # Adjust the position as needed
            size=(100, 100),  # Increase the size to make it bigger
            angle_start=0,
            angle_end=360,
            segments=360,  # Increase the number of segments for a smoother circle
        ))
        
        # Draw a smaller hollow ellipse on top
        self.canvas.after.add(Color(.8, .8, .8, 1))
        self.canvas.after.add(Ellipse(
            pos=(self.center_x - 25, self.center_y - 25),  # Adjust the position as needed
            size=(50, 50),  # Smaller size inside the filled ellipse
            angle_start=0,
            angle_end=360,
            segments=360,  # Increase the number of segments for a smoother circle
            width=13  # Set the width to create the hollow effect
        ))

class TTTGrid(GridLayout):
    def __init__(self, **kwargs):
        super(TTTGrid, self).__init__(**kwargs)
        self.padding = 25
        self.spacing = 25
        self.cols = 3
        self.rows = 3
        self.add_lines()
        self.add_squares()

    def add_lines(self):
        self.canvas.after.add(Color(0, 0, 0, 1))
        self.canvas.after.add(Line(points=[630 * (360/640), 25, 630 * (360/640), 515], width=13))
        self.canvas.after.add(Line(points=[650 * (360/640) / 2, 25, 650 * (360/640) / 2, 515], width=13))
        
        self.canvas.after.add(Line(points=[25, 630 * (360/640), 515, 630 * (360/640)], width=13))
        self.canvas.after.add(Line(points=[25, 650 * (360/640) / 2, 515, 650 * (360/640) / 2], width=13))


    def add_squares(self):
        for index in range(9):
            square = TTTSquare(index=index)
            self.add_widget(square)


class TTTBoard(RelativeLayout):
    def __init__(self, **kwargs):
        super(TTTBoard, self).__init__(**kwargs)
        self.size_hint_x = 360 / 640
        self.size_hint_y = 1
        self.squares = TTTGrid()
        self.add_widget(self.squares)
        self.reset_game()

    def reset_game(self):
        self.clear_widgets()
        self.squares = TTTGrid()
        self.add_widget(self.squares)
    

class Root(RelativeLayout):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.background = Background(color=(.8, .8, .8, 1))
        self.add_widget(self.background)
        self.board = TTTBoard()
        self.add_widget(self.board)


### KEEP CLASSES AS TEMPLATES BUT ADD CONSTRUCTOR THAT CREATES PARENTS/CHILDREN    
class TicTacToeApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    TicTacToeApp().run()