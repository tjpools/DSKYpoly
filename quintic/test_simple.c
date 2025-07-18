#include <stdio.h>

extern int solve_poly_5_special(double a, double b, double c, double d, double e, double f);

int main() {
    printf("Testing special solver...\n");
    int result = solve_poly_5_special(1.0, 0.0, 0.0, 0.0, 0.0, -32.0);
    printf("Result: %d\n", result);
    return 0;
}
