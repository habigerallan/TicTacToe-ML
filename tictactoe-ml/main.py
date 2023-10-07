import numpy as np
import random

from tictactoe import *

from NNBuilder import *
from NNlayers import *


def train(x, y):
	print(x)
	print(y)
	net = Network()
	net.add(FCLayer(9, 10))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(10, 1))
	net.add(ActivationLayer(tanh, tanh_prime))

	net.use(mse, mse_prime)
	net.fit(x, y, epochs=1000, learning_rate=0.1)

	return net

def main():
	game = TTTGame()
	net = None
	
	x_train = []
	y_train = []

	while (True):
		if (net):

			if (game.complete != 0):
				game = TTTGame()
				net = train(np.array(x_train), np.array(y_train))

			move = net.predict(game.board)
			max = -np.inf
			index = 0
			for i in range(9):
				curr_max = np.max(move[i])
				if (curr_max > max):
					index = i
			best_move = minimax.find_best_move(game)
			x_train.append([game.board])
			y_train.append([best_move])
			print(index)
			print(best_move)
			game.make_move(index)

			print(game)
			if (game.complete == 0):
				x_train.append([game.board])
				y_train.append([minimax.find_best_move(game)])
				move = int(input())
				game.make_move(move)
			else:
				game = Game()
				net = train(np.array(x_train), np.array(y_train))
		else:
			if (game.complete != 0):
				game = Game()
				net = train(np.array(x_train), np.array(y_train))

			possible_moves = []
			for i in range(9):
				if (game.board[i] == 0):
					possible_moves.append(i)
			move = random.choice(possible_moves)
			best_move = minimax.find_best_move(game)
			x_train.append([game.board])
			y_train.append([best_move])
			print(move)
			print(best_move)
			game.make_move(move)

			print(game)
			if (game.complete == 0):
				x_train.append([game.board])
				y_train.append([minimax.find_best_move(game)])
				move = int(input())
				game.make_move(move)
			else:
				game = Game()
				net = train(np.array(x_train), np.array(y_train))
			
 	
if __name__ == "__main__":
	main()