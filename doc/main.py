import random

import numpy as np

from tictactoe import *
from nn_builder import *
from nn_layers import *


def train(x, y):
	x = np.array(x)
	y = np.array(y)

	print("Training Started...")
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
	net.fit(x, y, epochs=1000, learning_rate=0.1)
	print("Training Complete.")
	return net

def setup_gui():
	pass

def is_over(game, net, x, y):
	if (game.complete != 0):
		print(game)
		print("Game Over!")
		print("Restarting...")
		net = train(x, y)
		game = TTTGame()
		return net, game, True

	return net, game, False

def get_data(game):
	x_temp = game.get_board_copy()
	y_temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	i = find_best_move(game)
	y_temp[i] = 1

	return x_temp, y_temp

def game_loop():
	game = TTTGame()
	net = None

	x_train = []
	y_train = []

	while (True):
		net, game, over = is_over(game, net, x_train, y_train)
		if (over):
			continue
		
		x_temp, y_temp = get_data(game)
		x_train.append(x_temp)
		y_train.append(y_temp)

		print(game)

		move = int(input("Enter your move: "))
		game.make_move(move)

		net, game, over = is_over(game, net, x_train, y_train)
		if (over):
			continue

		x_temp, y_temp = get_data(game)
		x_train.append(x_temp)
		y_train.append(y_temp)

		if (net):
			move_data = net.predict(np.array(game.board))
			move = np.argmax(move_data)
			print(f"picked move: {move}")
			print(f"best move: {find_best_move(game)}")
				
			move_lst = range(9)
			while (game.make_move(move) == -1):
				move = random.choice(move_lst)
		else:
			move_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
			move = random.choice(move_lst)
			while (game.make_move(move) == -1):
				move_lst.remove(move)
				move = random.choice(move_lst)
	
def main():
	setup_gui()
	game_loop()


if __name__ == '__main__':
	main()