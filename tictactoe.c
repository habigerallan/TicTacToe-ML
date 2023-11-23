#include <stdio.h>
#include <stdbool.h>

#define EMPTY 0b00
#define XPLAYER 0b01
#define OPLAYER 0b10

typedef struct {
    unsigned int board;
    unsigned int current_player;
    unsigned int winner;
    unsigned int score[2];
} Game;

void init_game(Game *game) {
    game->board = 0;
    game->current_player = XPLAYER;
    game->winner = 0;
    game->score[0] = 0;
    game->score[1] = 0;
}

unsigned int get_square(Game *game, int row, int col) {
    int pos = 6 * row + 2 * col;
    unsigned int mask = 0b11 << pos;
    return (game->board & mask) >> pos;
}

void set_square(Game *game, int row, int col) {
    int pos = 6 * row + 2 * col;
    game->board &= ~(0b11 << pos);
    game->board |= (game->current_player << pos);
}

void switch_player(Game *game) {
	if (game->current_player == XPLAYER) {
		game->current_player = OPLAYER;
	} else {
		game->current_player = XPLAYER;
	}
}

bool check_win(Game *game) {
    unsigned int board = game->board;

    if ((board & 0b111) == 0b111 || (board & 0b111000) == 0b111000 || (board & 0b111000000) == 0b111000000) {
        return true;
    }

    if ((board & 0b1001001) == 0b1001001 || (board & 0b101010) == 0b101010) {
        return true;
    }

    if ((board & 0b100010001) == 0b100010001 || (board & 0b1010101) == 0b1010101) {
        return true;
    }

    return false;
}


void make_move(Game *game, int row, int col) {
    if (get_square(game, row, col) != EMPTY) {
        return;
    }

    set_square(game, row, col);

    if (check_win(game)) {
        game->winner = game->current_player;
        game->score[game->current_player == XPLAYER ? 0 : 1]++;
    }

    switch_player(game);
}

