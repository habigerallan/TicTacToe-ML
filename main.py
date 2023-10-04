import sys
from game import Game
from minimax import Minimax

def main():
	b = Game()
	minimax = Minimax()

	while (b.complete == 0):
		print(b)
		move = int(input())
		b.make_move(move)

		if (b.complete == 0):
			minimax.find_best_move(b)
			b.make_move(minimax.move)
	print(b.complete)
	print(b)

 	
if __name__ == "__main__":
	main()