// game_of_life.c - Conway's Game of Life (terminal animation)
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define WIDTH 40
#define HEIGHT 20
#define ALIVE 'O'
#define DEAD  ' '
#define DELAY 100000

void print_board(char board[HEIGHT][WIDTH]) {
    printf("\033[H");
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            putchar(board[y][x]);
        }
        putchar('\n');
    }
}

int count_neighbors(char board[HEIGHT][WIDTH], int y, int x) {
    int count = 0;
    for (int dy = -1; dy <= 1; dy++)
        for (int dx = -1; dx <= 1; dx++)
            if ((dy || dx) &&
                y + dy >= 0 && y + dy < HEIGHT &&
                x + dx >= 0 && x + dx < WIDTH &&
                board[y + dy][x + dx] == ALIVE)
                count++;
    return count;
}

void step(char board[HEIGHT][WIDTH]) {
    char next[HEIGHT][WIDTH];
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            int n = count_neighbors(board, y, x);
            if (board[y][x] == ALIVE)
                next[y][x] = (n == 2 || n == 3) ? ALIVE : DEAD;
            else
                next[y][x] = (n == 3) ? ALIVE : DEAD;
        }
    }
    for (int y = 0; y < HEIGHT; y++)
        for (int x = 0; x < WIDTH; x++)
            board[y][x] = next[y][x];
}

void seed_board(char board[HEIGHT][WIDTH]) {
    srand(time(NULL));
    for (int y = 0; y < HEIGHT; y++)
        for (int x = 0; x < WIDTH; x++)
            board[y][x] = (rand() % 5 == 0) ? ALIVE : DEAD;
}

int main() {
    char board[HEIGHT][WIDTH];
    seed_board(board);
    printf("\033[2J"); // clear screen
    while (1) {
        print_board(board);
        step(board);
        usleep(DELAY);
    }
    return 0;
}
