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
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line, Ellipse

import random
import numpy as np

from tictactoe import *
from nn_builder import *
from nn_layers import *

def create_network() -> Network:
	net = Network()
	net.add(FCLayer(9, 12))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(12, 21))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(21, 12))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(12, 9))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.use(mse, mse_prime)

	return net


def train(net, x, y) -> None:
	x = np.array(x)
	y = np.array(y)

	print((f"Training on {len(x)} games..."))

	net.fit(x, y, epochs=1000, learning_rate=0.1)


def setup_gui():
	pass


def is_game_over(game) -> bool:
	if (game.complete != 0):
		print("Game Over!")
		print("Restarting...")
		return True
	
	return False


def get_data(game) -> (list, list):
	x_temp = game.get_board_copy()
	y_temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	index = find_best_move(game)
	y_temp[index] = 1

	return x_temp, y_temp

class Root(RelativeLayout):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.size = Window.size
        self.pos = (0,0)

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

        self.game = TTTGame()
        self.net = create_network()
        self.x_train = []
        self.y_train = []

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
        self.game = TTTGame()
        
class GameCell(Button):
    def __init__(self, index, **kwargs):
        super(GameCell, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (1, 1, 1, 1)
        self.index = index        
        self.filled = False

        self.bind(on_press=self.mouse1_down)

    def mouse1_down(self, cell):
        game = cell.parent.game
        net = cell.parent.net
        x_train = cell.parent.x_train
        y_train = cell.parent.y_train
        if (cell.filled == False and game.complete == 0):
            cell.filled = True

            cell.draw_x(cell)
            # PLAYER MOVE
            x_temp, y_temp = get_data(game)
            x_train.append(x_temp)
            y_train.append(y_temp)

            game.make_move(cell.index)

            if (is_game_over(game)):
                train(net, x_train, y_train)
                cell.parent.clear_cells()
                return


            # AI MOVE
            x_temp, y_temp = get_data(game)
            x_train.append(x_temp)
            y_train.append(y_temp)

            move_data = net.predict(np.array(game.board))
            move = np.argmax(move_data)

            move_lst = range(9)
            while (game.make_move(move) == -1):
                move = random.choice(move_lst)

            for i in range(9):
                if (cell.parent.cells[i].index == move):
                    ai_cell = cell.parent.cells[i]
                    
                    ai_cell.filled = True

                    ai_cell.draw_o(ai_cell)

                    if (is_game_over(game)):
                        train(net, x_train, y_train)
                        ai_cell.parent.clear_cells()
                        return


    def draw_x(self, cell):
        with cell.canvas.after:
            Color(0, 0, 0, 1)
            Line(points=[cell.x, cell.y, cell.right, cell.top], width=10)
            Line(points=[cell.x, cell.top, cell.right, cell.y], width=10)


    def draw_o(self, cell):
        with cell.canvas.after:
            Color(1, 1, 1, 1)
            Ellipse(pos=cell.pos, size=cell.size)
            Color(0, 0, 0, 1)
            Line(circle=[cell.center_x, cell.center_y, min(cell.width, cell.height) / 2], width=10)

class TicTacToeApp(App):
    def build(self):
        Window.size = (640, 360)

        root = Root()
        root_bg = Background(color=(1,1,1,1), parent=root)
        root.add_widget(root_bg)

        game_frame = GameFrame()
        game_frame_bg = Background(color=(0,0,0,.1), parent=game_frame)
        game_frame.add_widget(game_frame_bg)
        root.add_widget(game_frame)

        game_layout = GameLayout()
        game_frame.add_widget(game_layout)
        return root

if __name__ == '__main__':
    TicTacToeApp().run()