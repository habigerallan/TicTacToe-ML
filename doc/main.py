import random

import numpy as np

from tictactoe import *
from nn_builder import *
from nn_layers import *


def train(x, y):
	print(x)
	print(y)
	net = Network()
	net.add(FCLayer(1, 1))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(1, 1))
	net.add(ActivationLayer(tanh, tanh_prime))

	net.use(mse, mse_prime)
	net.fit(x, y, epochs=1000, learning_rate=0.1)

	return net

def setup_gui():
	pass

def game_loop():
	game = TTTGame()
	net = None
	train(np.array([0]), np.array([0]))
	
	x_train = []
	y_train = []

	

def main():
	setup_gui()
	game_loop()


if __name__ == '__main__':
	main()