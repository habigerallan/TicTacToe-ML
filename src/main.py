from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

from player import Player, PlayerType
from game import Game

class TicTacToeApp(App):
	def build(self):
		self.game = Game(Player(PlayerType.PLAYER), Player(PlayerType.PLAYER))
		self.board = GridLayout(spacing=(10,10), cols=3)

		for i in range(9):
			button = Button(background_normal='', background_color=(.2,.2,.2,1))
			button.bg_color = (0.2, 0.2, 0.2, 1)
			button.bind(on_press=self.board_clicked, size=self.draw_rect, pos=self.draw_rect)
			with button.canvas.before:
				Color(*button.bg_color)
				button.rect = Rectangle(size=button.size, pos=button.pos)

			self.board.add_widget(button)

		container = BoxLayout(width=300, height=300)
		container.bg_color = (1, 1, 1, 1)
		container.bind(size=self.draw_rect, pos=self.draw_rect)
		with container.canvas.before:
				Color(*container.bg_color)
				container.rect = Rectangle(size=container.size, pos=container.pos)

		container.add_widget(self.board)

		return container

	def board_clicked(self, instance):
		pass

	def change_x_player(self, instance):
		pass

	def change_o_player(self, instance):
		pass

	def restart_game(self, instance):
		pass

	def draw_rect(self, instance, value):
		instance.canvas.before.clear()
		with instance.canvas.before:
			Color(*instance.bg_color)
			instance.rect = Rectangle(size=instance.size, pos=instance.pos)

if __name__ == '__main__':
	TicTacToeApp().run()
