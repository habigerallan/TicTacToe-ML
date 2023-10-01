import sys
from game import Game
from minimax import Minimax

def main():
	sys.setrecursionlimit(1000000000)
	b = Game()
	minimax = Minimax()

	b.make_move(0)
	b.make_move(3)
	b.make_move(1)
 
	minimax.find_best_move(b)
	best_move = minimax.move
 
	print(best_move)
	#b.make_move(best_move)
	print(b.board)
	
if __name__ == "__main__":
	main()