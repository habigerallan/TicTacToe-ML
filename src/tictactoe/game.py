from tictactoe.player import Player
import numpy as np
import copy

class Game:
	def __init__(self, x_player: Player, o_player: Player) -> None:
		self.board = np.zeros(9, dtype=int)
		self.x_player = x_player
		self.o_player = o_player
		self.current_player = self.x_player
		self.game_over = False
		self.winner = None

	def set_x_player(self, new_player: Player) -> None:
		if (self.current_player == self.x_player):
			self.current_player = new_player

		self.x_player = new_player

	def set_o_player(self, new_player: Player) -> None:
		if (self.current_player == self.o_player):
			self.current_player = new_player

		self.o_player = new_player

	def check_win(self) -> None:
		for i in range(0, 9, 3):
			if abs(self.board[i] + self.board[i + 1] + self.board[i + 2]) == 3:
				self.game_over = True
				self.winner = self.current_player
				return

		for i in range(3):
			if abs(self.board[i] + self.board[i + 3] + self.board[i + 6]) == 3:
				self.game_over = True
				self.winner = self.current_player
				return

		if abs(self.board[0] + self.board[4] + self.board[8]) == 3 or abs(self.board[2] + self.board[4] + self.board[6]) == 3:
			self.game_over = True
			self.winner = self.current_player
			return

		if 0 not in self.board:
			self.game_over = True
			self.winner = None
			
	def make_move(self, move_index: int) -> bool:
		if (self.board[move_index] == 0):
			if (self.current_player == self.x_player):
				self.board[move_index] = 1
			else:
				self.board[move_index] = -1

			if (self.current_player == self.x_player):
				self.current_player = self.o_player  
			else:
				self.current_player = self.x_player

			self.check_win()

			return True

		return False

	def reset_game(self) -> None:
		self.board = np.zeros(9, dtype=int)
		self.current_player = self.x_player
		self.game_over = False
		self.winner = None

	def get_board(self) -> list:
		return copy.deepcopy(self.board)

	def get_x_player(self) -> Player:
		return self.x_player

	def get_o_player(self) -> Player:
		return self.o_player

	def get_current_player(self) -> Player:
		return self.current_player

	def get_game_over(self) -> bool:
		return self.game_over
