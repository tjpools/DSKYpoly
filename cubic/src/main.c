// === main.c for DSKYpoly-3 ===
// Symbolic interface for solving cubic equations

#include <stdio.h>
#include <stdlib.h>

// Declare the external assembly function
extern void solve_cubic(double a, double b, double c, double d);

int main() {
    double a, b, c, d;

    printf("=== DSKYpoly Cubic Solver ===\n");
    printf("Enter coefficients for ax³ + bx² + cx + d = 0\n");

    printf("A: ");
    if (scanf("%lf", &a) != 1 || a == 0.0) {
        fprintf(stderr, "Invalid input. Coefficient 'a' must be non-zero.\n");
        return 1;
    }

    printf("B: ");
    scanf("%lf", &b);
    printf("C: ");
    scanf("%lf", &c);
    printf("D: ");
    scanf("%lf", &d);

    printf("\nSolving: %.4fx³ + %.4fx² + %.4fx + %.4f = 0\n", a, b, c, d);

    // Call the symbolic solver
    solve_cubic(a, b, c, d);

    return 0;
}
