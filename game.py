import warnings

class Game:
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
			d1, d2 = (0, 0)
			
			for i in range(3):
				r1 += self.board[i]
				r2 += self.board[i+3]
				r3 += self.board[i+6]
				
				c1 += self.board[i*3]
				c2 += self.board[i*3+1]
				c3 += self.board[i*3+2]
				
				d1 += self.board[i*4]
				d2 += self.board[i*2+2]
			
			x_total = max(r1, r2, r3, c1, c2, c3, d1, d2)
			o_total = min(r1, r2, r3, c1, c2, c3, d1, d2)
			
			# X Win
			if (x_total == 3):
				self.complete = 1

			# O Win
			if (o_total == -3):
				self.complete = 2
				
			# Tie Case
			if (abs(r1) == 1 and abs(r2) == 1 and abs(r3) == 1):
				self.complete = 3
			
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
		g_copy = Game()
  
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
	