// rotation_matrix.c - Animated 2D triangle rotation using matrix multiplication
#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include <stdlib.h>

#define PI 3.14159265358979323846
#define FRAMES 60
#define DELAY 80000
#define WIDTH 40
#define HEIGHT 20

// 2D point structure
typedef struct { double x, y; } Point;

// Map world coordinates to screen
void to_screen(Point p, int *sx, int *sy) {
    *sx = (int)(WIDTH/2 + p.x * (WIDTH/4));
    *sy = (int)(HEIGHT/2 - p.y * (HEIGHT/4));
}

// Draw triangle on ASCII grid
void draw_triangle(Point pts[3]) {
    char grid[HEIGHT][WIDTH];
    for (int y = 0; y < HEIGHT; y++)
        for (int x = 0; x < WIDTH; x++)
            grid[y][x] = ' ';
    for (int i = 0; i < 3; i++) {
        int sx, sy;
        to_screen(pts[i], &sx, &sy);
        if (sx >= 0 && sx < WIDTH && sy >= 0 && sy < HEIGHT)
            grid[sy][sx] = '*';
    }
    // Draw lines (simple Bresenham)
    for (int i = 0; i < 3; i++) {
        int x0, y0, x1, y1;
        to_screen(pts[i], &x0, &y0);
        to_screen(pts[(i+1)%3], &x1, &y1);
        int dx = abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
        int dy = -abs(y1 - y0), sy = y0 < y1 ? 1 : -1;
        int err = dx + dy, e2;
        while (1) {
            if (x0 >= 0 && x0 < WIDTH && y0 >= 0 && y0 < HEIGHT)
                grid[y0][x0] = '*';
            if (x0 == x1 && y0 == y1) break;
            e2 = 2 * err;
            if (e2 >= dy) { err += dy; x0 += sx; }
            if (e2 <= dx) { err += dx; y0 += sy; }
        }
    }
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++)
            putchar(grid[y][x]);
        putchar('\n');
    }
}

// Rotate a point by theta radians
Point rotate(Point p, double theta) {
    double c = cos(theta), s = sin(theta);
    return (Point){ p.x * c - p.y * s, p.x * s + p.y * c };
}

int main() {
    Point tri[3] = { {0,1}, {-0.866,-0.5}, {0.866,-0.5} };
    for (int frame = 0; frame < FRAMES; frame++) {
        printf("\033[H\033[2J");
        double theta = 2 * PI * frame / FRAMES;
        Point rot[3];
        for (int i = 0; i < 3; i++)
            rot[i] = rotate(tri[i], theta);
        printf("Frame %d / %d\n", frame+1, FRAMES);
        draw_triangle(rot);
        fflush(stdout);
        usleep(DELAY);
    }
    return 0;
}
