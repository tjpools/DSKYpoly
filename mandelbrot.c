// mandelbrot.c - Mandelbrot set ASCII visualization
#include <stdio.h>

#define WIDTH 80
#define HEIGHT 24
#define MAX_ITER 1000

int mandelbrot(double cr, double ci) {
    double zr = 0.0, zi = 0.0;
    int iter = 0;
    while (zr * zr + zi * zi < 4.0 && iter < MAX_ITER) {
        double tmp = zr * zr - zi * zi + cr;
        zi = 2.0 * zr * zi + ci;
        zr = tmp;
        iter++;
    }
    return iter;
}

int main() {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            double cr = (x - WIDTH / 2.0) * 4.0 / WIDTH;
            double ci = (y - HEIGHT / 2.0) * 2.0 / HEIGHT;
            int iter = mandelbrot(cr, ci);
            char c = (iter == MAX_ITER) ? '#' : " .-~:;=!*#$@"[iter % 11];
            putchar(c);
        }
        putchar('\n');
    }
    return 0;
}
