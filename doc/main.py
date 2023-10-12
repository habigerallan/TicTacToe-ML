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

	print("Training Complete.")


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


def game_loop() -> None:
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

		
		# Player Move
		move_lst = range(9)

		try: 
			move = int(input("Enter your move: "))
		except ValueError:
			move = random.choice(move_lst)
		
		if (move < 0 and 8 < move):
			move = random.choice(move_lst)

		while (game.make_move(move) == -1):
			move = random.choice(move_lst)

		print(f"Picked move: {move}")
		print(f"Best move: {find_best_move(game)}")


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
		while (game.make_move(move) == -1):
			move = random.choice(move_lst)

		print(f"Picked move: {move}")
		print(f"Best move: {find_best_move(game)}")


def main():
	setup_gui()
	game_loop()


if __name__ == '__main__':
	main()