import random
import threading

import numpy as np

from tictactoe import *
from nn_builder import *
from nn_layers import *
from app import *


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

def setup_gui() -> object:
	return TicTacToeApp()

def game_loop(ttt_app) -> None:
	app = ttt_app
	game_layout = app.game_layout

	game = TTTGame()
	net = create_network()

	x_train = []
	y_train = []
	
	while (True):
		# Game Handling
		print(game)

		if (is_game_over(game)):
			game = TTTGame()
			train(net, x_train, y_train)
			continue
		
		x_temp, y_temp = get_data(game)
		x_train.append(x_temp)
		y_train.append(y_temp)

		made_move = False
		while made_move:
			for i in range(9): 
				if game_layout.cells[i].selected:
					game_layout.cells[i].selected = False
					game_layout.cells[i].filled = True

					if game.move_value == 1:
						game_layout.cells[i].draw_x()
					else:
						game_layout.cells[i].draw_o()

					game.make_move(i)
					made_move = True

					break

		# Player Move
		# move_lst = range(9)

		# try: 
		# 	move = int(input("Enter your move: "))
		# except ValueError:
		# 	move = random.choice(move_lst)
		
		# if (move < 0 or 8 < move):
		# 	move = random.choice(move_lst)

		# while (game.make_move(move) == -1):
		# 	move = random.choice(move_lst)

		# print(f"Picked move: {move}")
		# print(f"Best move: {find_best_move(game)}")


		# Game Handling
		print(game)

		if (is_game_over(game)):
			game = TTTGame()
			train(net, x_train, y_train)
			continue
		
		x_temp, y_temp = get_data(game)
		x_train.append(x_temp)
		y_train.append(y_temp)


		# AI Move
		move_data = net.predict(np.array(game.board))
		move = np.argmax(move_data)

		move_lst = range(9)
		while (game.board[move] != 0):
			move = random.choice(move_lst)

		game_layout.cells[move].selected = False
		game_layout.cells[move].filled = True

		if game.move_value == 1:
			game_layout.cells[move].draw_x()
		else:
			game_layout.cells[move].draw_o()

		game.make_move(move)
		
		print(f"Picked move: {move}")
		print(f"Best move: {find_best_move(game)}")


def main() -> None:
	app = setup_gui()
	threading.Thread(target=game_loop, args=[app]).start()
	app.run()
	


if __name__ == '__main__':
	main()