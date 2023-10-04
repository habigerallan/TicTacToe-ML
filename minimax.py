class Minimax:
	def __init__(self):
		self.move = -1
	
	def score(self, game, depth):
		if (game.complete == 1):
			return 10 - depth
		elif (game.complete == 2):
			return depth - 10
		elif (game.complete == 3):
			return 0
	
	def find_best_move(self, game, depth=0) -> int:
		if (game.complete != 0):
			return self.score(game, depth)
		
		scores = []
		moves = []
  
		for move in range(9):
			if (game.board[move] == 0):
				possible_game = game.get_copy()
				possible_game.make_move(move)
				scores.append(self.find_best_move(possible_game, depth+1))
				moves.append(move)	

		if (game.move_value == 1):
			index = scores.index(max(scores))
			self.move = moves[index]
			return scores[index]
		else:
			index = scores.index(min(scores))
			self.move = moves[index]
			return scores[index]