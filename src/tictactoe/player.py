from enum import Enum

class PlayerType(Enum):
	PLAYER = 0
	CPU = 1

class Player:
	def __init__(self, player_type: PlayerType) -> None:
		self.player_type = player_type

	def is_player(self) -> bool:
		return (self.player_type == PlayerType.PLAYER)

	def is_cpu(self) -> bool:
		return (self.player_type == PlayerType.CPU)
