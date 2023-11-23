import ctypes

class Game(ctypes.Structure):
	_fields_ = [("board", ctypes.c_uint),
				("current_player", ctypes.c_uint),
				("winner", ctypes.c_uint),
				("score", ctypes.c_uint * 2)]

tictactoe = ctypes.CDLL(name="./tictactoe.dll")

tictactoe.init_game.argtypes = [ctypes.POINTER(Game)]
tictactoe.get_square.argtypes = [ctypes.POINTER(Game), ctypes.c_int, ctypes.c_int]
tictactoe.get_square.restype = ctypes.c_uint
tictactoe.set_square.argtypes = [ctypes.POINTER(Game), ctypes.c_int, ctypes.c_int]
tictactoe.switch_player.argtypes = [ctypes.POINTER(Game)]
tictactoe.check_win.argtypes = [ctypes.POINTER(Game)]
tictactoe.check_win.restype = ctypes.c_bool
tictactoe.make_move.argtypes = [ctypes.POINTER(Game), ctypes.c_int, ctypes.c_int]

game = Game()
tictactoe.init_game(ctypes.byref(game))
tictactoe.make_move(ctypes.byref(game), 0, 0)

symbols = {0b00: " . ", 0b01: " X ", 0b10: " O "}
for row in range(3):
	for col in range(3):
		square = tictactoe.get_square(ctypes.byref(game), row, col)
		print(symbols[square], end='')
	print() 
print()