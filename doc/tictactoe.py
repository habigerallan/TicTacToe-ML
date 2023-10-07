import warnings

def score(game, depth):
		if (game.complete == 1):
			return 10 - depth
		elif (game.complete == 2):
			return depth - 10
		elif (game.complete == 3):
			return 0
	
def find_best_move(game, depth=0, move=None) -> int:
	if (game.complete != 0):
		return score(game, depth)
	
	scores = []
	moves = []

	for move in range(9):
		if (game.board[move] == 0):
			possible_game = game.get_copy()
			possible_game.make_move(move)
			scores.append(find_best_move(possible_game, depth+1, move))
			moves.append(move)	

	if (game.move_value == 1):
		index = scores.index(max(scores))
		move = moves[index]

		if (depth == 0):
			return move
		
		return scores[index]
	else:
		index = scores.index(min(scores))
		move = moves[index]

		if (depth == 0):
			return move
		
		return scores[index]

class TTTGame:
	def __init__(self) -> None:
		self.board = [0, 0, 0,
					  0, 0, 0,
					  0, 0, 0]
		
		self.move_value = 1
		self.complete = 0
		
	def update_state(self) -> None:
		if (self.complete == 0):
			r1, r2, r3 = (0, 0, 0)
			c1, c2, c3 = (0, 0, 0)
			t1, t2, t3 = (0, 0, 0)
			d1, d2 = (0, 0)

			for i in range(3):
				r1 += self.board[i]
				r2 += self.board[i+3]
				r3 += self.board[i+6]
				
				c1 += self.board[i*3]
				c2 += self.board[i*3+1]
				c3 += self.board[i*3+2]

				t1 += abs(self.board[i])
				t2 += abs(self.board[i+3])
				t3 += abs(self.board[i+6])

				d1 += self.board[i*4]
				d2 += self.board[i*2+2]
			
			x_total = max(r1, r2, r3, c1, c2, c3, d1, d2)
			o_total = min(r1, r2, r3, c1, c2, c3, d1, d2)
			
			# X Win
			if (x_total == 3):
				self.complete = 1

			# O Win
			elif (o_total == -3):
				self.complete = 2
				
			# Tie Case
			elif (t1 == 3 and t2 == 3 and t3 == 3):
					self.complete = 3

	def is_valid(self, index) -> bool:
		return (self.board[index] == 0)
			
	def make_move(self, index) -> None:
		if (self.complete != 0):
			warnings.warn("Attempted Move On Completed Board")
			exit(-1)	
		
		if (self.board[index] == 0):
			self.board[index] = self.move_value
			self.move_value = -self.move_value
			self.update_state()
		else:
			warnings.warn("Invalid Move Selection")
			exit(-1)			
			
	def get_copy(self) -> object:
		g_copy = TTTGame()
  
		new_board = []
		for i in self.board:
			new_board.append(i)
   
		g_copy.board = new_board
		g_copy.move_value = self.move_value
		g_copy.complete = self.complete
		
		return g_copy
					
	def __str__(self) -> str:
		r_str = ""
		
		for i in range(9):
			if self.board[i] == -1:
				r_str += " O "
			elif self.board[i] == 0:
				r_str += " # "
			else:
				r_str += " X "
			
			if (i == 2 or i == 5):
				r_str += "\n"
				
		return r_str
	