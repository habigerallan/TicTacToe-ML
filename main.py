import sys
from game import Game
from minimax import Minimax

def main():
	b = Game()
	minimax = Minimax()

	while (b.complete == 0):
		minimax.find_best_move(b)
		b.make_move(minimax.move)
		print(b)
		if (b.complete == 0):
			move = int(input())
			move = 0 if move == 7 else 1 if move == 8 else 2 if move == 9 else 3 if move == 4 else 4 if move == 5 else 5 if move == 6 else 6 if move == 1 else 7 if move == 2 else 8 if move == 3 else None
			b.make_move(move)

		
	print(b.complete)
	print(b)

 	
if __name__ == "__main__":
	main()