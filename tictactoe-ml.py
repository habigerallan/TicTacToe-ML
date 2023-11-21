import pygame as pg
import sys

CAPTION = "Tic-Tac-Toe"
SCREEN_SIZE = (450, 300)  # Increased width for the menu
BOARD_SIZE = (300, 300)
CELL_SIZE = BOARD_SIZE[0] // 3, BOARD_SIZE[1] // 3
MENU_WIDTH = SCREEN_SIZE[0] - BOARD_SIZE[0]

COLORS = {"background": (30, 40, 50), "line": (200, 200, 200), "menu": (50, 60, 70)}

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.score = {'X': 0, 'O': 0}

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if self.board[row][col] == '' and self.winner is None:
            self.board[row][col] = self.current_player
            if self.check_win():
                self.winner = self.current_player
                self.score[self.current_player] += 1
            self.switch_player()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.winner = None

def draw_board(screen, game):
    screen.fill(COLORS["background"])
    # Draw the Tic-Tac-Toe board
    for x in range(1, 3):
        pg.draw.line(screen, COLORS["line"], (x * CELL_SIZE[0], 0), (x * CELL_SIZE[0], BOARD_SIZE[1]), 2)
        pg.draw.line(screen, COLORS["line"], (0, x * CELL_SIZE[1]), (BOARD_SIZE[0], x * CELL_SIZE[1]), 2)

    for row in range(3):
        for col in range(3):
            mark = game.board[row][col]
            if mark:
                center_x = col * CELL_SIZE[0] + CELL_SIZE[0] // 2
                center_y = row * CELL_SIZE[1] + CELL_SIZE[1] // 2
                if mark == 'X':
                    pg.draw.line(screen, COLORS["line"], (center_x - 40, center_y - 40), (center_x + 40, center_y + 40), 2)
                    pg.draw.line(screen, COLORS["line"], (center_x + 40, center_y - 40), (center_x - 40, center_y + 40), 2)
                else:
                    pg.draw.circle(screen, COLORS["line"], (center_x, center_y), 40, 2)

    # Draw the menu
    menu_rect = pg.Rect(BOARD_SIZE[0], 0, MENU_WIDTH, SCREEN_SIZE[1])
    pg.draw.rect(screen, COLORS["menu"], menu_rect)

    # Draw the score
    font = pg.font.Font(None, 36)
    score_text = f'X: {game.score["X"]} - O: {game.score["O"]}'
    score_surface = font.render(score_text, True, pg.Color("white"))
    score_rect = score_surface.get_rect(center=(BOARD_SIZE[0] + MENU_WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)

    # Draw the reset button
    reset_button = pg.Rect(BOARD_SIZE[0] + 10, 250, MENU_WIDTH - 20, 40)
    pg.draw.rect(screen, COLORS["line"], reset_button)
    reset_text = font.render("Reset", True, pg.Color("black"))
    reset_rect = reset_text.get_rect(center=reset_button.center)
    screen.blit(reset_text, reset_rect)

    return reset_button

def main():
    pg.init()
    pg.display.set_caption(CAPTION)
    screen = pg.display.set_mode(SCREEN_SIZE)
    game = TicTacToe()
    clock = pg.time.Clock()
    done = False
    reset_button = None

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if reset_button and reset_button.collidepoint(x, y):
                    game.reset()
                elif x < BOARD_SIZE[0] and game.winner is None:  # Click on the board
                    row = y // CELL_SIZE[1]
                    col = x // CELL_SIZE[0]
                    game.make_move(row, col)

        reset_button = draw_board(screen, game)
        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
