#include <stdio.h>
#include <stdlib.h>

extern int solve_poly_5_special(double a, double b, double c, double d, double e, double f);

// Testing the boundary of algebraic solvability
// This polynomial: x^5 - 32 = 0 has solutions x = 2·ω^k (5th roots of unity)
// It represents a solvable quintic - one of the rare cases where radicals suffice
// This test probes the liminal space between Abel-Ruffini impossibility and special solvability

int main() {
    printf("Testing minimal assembly call...\n");
    printf("Polynomial: x^5 - 32 = 0 (solvable quintic)\n");
    printf("Expected roots: x = 2·ω^k where ω = e^(2πi/5)\n");
    fflush(stdout);
    
    printf("About to call assembly function...\n");
    fflush(stdout);
    
    int result = solve_poly_5_special(1.0, 0.0, 0.0, 0.0, 0.0, -32.0);
    
    printf("Assembly function returned: %d\n", result);
    printf("(This tests the boundary between solvable and unsolvable quintics)\n");
    fflush(stdout);
    
    return 0;
}
