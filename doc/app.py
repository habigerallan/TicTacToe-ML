from kivy.app import App
from kivy.uix.widget import Widget

class TicTacToeWidget(Widget):
    pass


class TicTacToeApp(App):
    def build(self):
        return TicTacToeWidget()


if __name__ == '__main__':
    TicTacToeApp().run()