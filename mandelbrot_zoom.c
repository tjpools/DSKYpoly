// mandelbrot_zoom.c - Animated Mandelbrot set zoom with rich ASCII emergence
#include <stdio.h>
#include <unistd.h>

#define WIDTH 80
#define HEIGHT 24
#define MAX_ITER 1000
#define FRAMES 60
#define ZOOM_FACTOR 0.92

const char *palette = " .:-=+*#%@";

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

void draw(double cx, double cy, double scale) {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            double cr = cx + (x - WIDTH / 2.0) * scale;
            double ci = cy + (y - HEIGHT / 2.0) * scale * (double)HEIGHT / WIDTH;
            int iter = mandelbrot(cr, ci);
            char c = palette[(iter == MAX_ITER) ? 9 : (iter % 10)];
            putchar(c);
        }
        putchar('\n');
    }
}

int main() {
    double cx = -0.7436438870371587; // Deep zoom point
    double cy = 0.13182590420533;
    double scale = 4.0 / WIDTH;
    for (int frame = 0; frame < FRAMES; frame++) {
        printf("\033[H\033[2J"); // Clear screen
        printf("Frame %d / %d\n", frame + 1, FRAMES);
        draw(cx, cy, scale);
        fflush(stdout);
        usleep(120000);
        scale *= ZOOM_FACTOR;
    }
    return 0;
}
