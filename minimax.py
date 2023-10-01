class Minimax:
	def __init__(self):
		self.move = -1
	
	def score(self, game, depth):
		if (game.complete == 1):
			return 1 - depth
		elif (game.complete == 2):
			return depth -1
		elif (game.complete == 3):
			return 0
	
	def find_best_move(self, game, depth=0) -> int:
		if (game.complete != 0):
			return game.score(game, depth)
		
		depth += 1
		scores = []
		moves = []
		
		for move in range(9):
			possible_game = game.get_copy()
			
			if (possible_game.board[move] == 0):
				possible_game.make_move(move)
				scores.append(self.find_best_move(game, depth))
				moves.append(move)				
        
		if (game.move_value == 1):
			index = scores.pop(max(scores))
			self.move = moves[index]
			return scores[index]
		else:
			index = scores.pop(min(scores))
			self.move = moves[index]
			return scores[index]