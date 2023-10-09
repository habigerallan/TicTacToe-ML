import random

import numpy as np

from tictactoe import *
from nn_builder import *
from nn_layers import *


def train(x, y):
	print(x)
	print(y)
	net = Network()
	net.add(FCLayer(9, 9))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(9, 1))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.use(mse, mse_prime)
	net.fit(x, y, epochs=1000, learning_rate=0.1)

	return net

def setup_gui():
	pass

def game_loop():
	game = TTTGame()
	net = None

	x_train = np.array([])
	y_train = np.array([])

	train([0,0,0,0,0,0,0,0,0],[1])
	return
	while (True):
		if (game.complete != 0):
			print('Game Over!')
			net = train(x_train, y_train)
			game = TTTGame()

		x_train.append(game.board)
		y_train.append(find_best_move(game))

		print(game)

		move = int(input("Enter your move: "))
		game.make_move(move)
		
		if (game.complete != 0):
			print('Game Over!')
			net = train(x_train, y_train)
			game = TTTGame()

		x_train.append(game.board)
		y_train.append(find_best_move(game))

		print(game)

		if (net == None):
			print("no nn")
			move_lst = range(9)
			move = random.choice(move_lst)
			while (game.make_move(move) != 1):
				move = random.choice(move_lst)
		else:
			print("nn loaded")
			move = net.predict(game.board)
			print(move)
	

def main():
	setup_gui()
	game_loop()


if __name__ == '__main__':
	main()