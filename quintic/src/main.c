/*
 * DSKYpoly-5: Quintic Polynomial Solver
 * Mathematical Foundation: Abel-Ruffini Theorem + Galois Theory
 * 
 * Where radical solvability meets algebraic impossibility
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Forward declarations for assembly functions
extern void solve_poly_5_reference(double a, double b, double c, double d, double e, double f);
extern int solve_poly_5_special(double a, double b, double c, double d, double e, double f);

// Test case structure for quintic polynomials
typedef struct {
    double coeffs[6];  // a, b, c, d, e, f for ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0
    char description[100];
    char expected[200];
    char mathematical_significance[300];
} quintic_test_case;

// Quintic test cases covering the mathematical spectrum
static quintic_test_case test_cases[] = {
    // Solvable Cases (Special Forms)
    {
        {1.0, 0.0, 0.0, 0.0, 0.0, -32.0},  // x^5 - 32 = 0
        "Monomial quintic (solvable)",
        "x = 2ω^k where ω = e^(2πi/5), k = 0,1,2,3,4",
        "Solvable by radicals: x^5 = 32 → x = 2 · (5th roots of unity)"
    },
    {
        {1.0, 0.0, 0.0, 0.0, 5.0, -6.0},   // x^5 + 5x - 6 = 0  
        "Binomial quintic (Bring-Jerrard form)",
        "Requires elliptic functions or numerical methods",
        "Special binomial case - historically significant for transcendental methods"
    },
    
    // General Cases (Require Numerical Methods)
    {
        {1.0, -5.0, 5.0, 5.0, -5.0, -1.0}, // x^5 - 5x^4 + 5x^3 + 5x^2 - 5x - 1 = 0
        "General quintic (unsolvable by radicals)",
        "Numerical approximation required",
        "Demonstrates Abel-Ruffini theorem: no radical formula exists"
    },
    {
        {1.0, 0.0, -10.0, 0.0, 5.0, 0.0},  // x^5 - 10x^3 + 5x = 0
        "Odd quintic (factorizable)",
        "x(x^4 - 10x^2 + 5) = 0",
        "Factorizable case: x=0 and quartic subproblem"
    },
    {
        {1.0, 1.0, 1.0, 1.0, 1.0, 1.0},    // x^5 + x^4 + x^3 + x^2 + x + 1 = 0
        "Cyclotomic-related quintic",
        "Complex roots near 6th roots of unity",
        "Related to (x^6 - 1)/(x - 1) = 0, demonstrates complex root structure"
    }
};

static const int num_test_cases = sizeof(test_cases) / sizeof(test_cases[0]);

// Display mathematical context for quintic solving
void display_quintic_context(void) {
    printf("╔═══════════════════════════════════════════════════════════════╗\n");
    printf("║                    DSKYpoly-5 Quintic Solver                  ║\n");
    printf("║              Abel-Ruffini Theorem + Galois Theory             ║\n");
    printf("╠═══════════════════════════════════════════════════════════════╣\n");
    printf("║ Transforms: ax⁵ + bx⁴ + cx³ + dx² + ex + f = 0                ║\n");
    printf("║ Theory: No general radical solution (Abel-Ruffini, 1824-1826) ║\n");
    printf("║ Implementation: Numerical methods + special case detection    ║\n");
    printf("╚═══════════════════════════════════════════════════════════════╝\n\n");
    
    printf("🏛️ Mathematical Foundation:\n");
    printf("   • Galois Group S₅: 120 permutations, contains non-solvable A₅\n");
    printf("   • Abel-Ruffini Theorem: General quintic unsolvable by radicals\n");
    printf("   • Special Cases: Monomial, certain binomial forms ARE solvable\n");
    printf("   • Numerical Methods: Newton-Raphson, Durand-Kerner for general case\n\n");
}

// Display Galois theory insights
void display_galois_insights(void) {
    printf("🧮 Galois Theory Context:\n");
    printf("─────────────────────────────────────────────────────────────────\n");
    printf("Group Theory and Solvability:\n");
    printf("  • S₅ (Symmetric): 120 elements, all permutations of 5 objects\n"); 
    printf("  • A₅ (Alternating): 60 even permutations, simple non-solvable subgroup\n");
    printf("  • Solvable Subgroups: Only those avoiding A₅ allow radical solutions\n");
    printf("  • Fundamental Insight: Equation solvability ↔ Galois group solvability\n\n");
    
    printf("Historical Impact:\n");
    printf("  • End of 300-year search for quintic formula (like quadratic formula)\n");
    printf("  • Birth of abstract algebra and group theory\n");
    printf("  • Demonstrated fundamental limits of algebraic methods\n\n");
}

// Test a single quintic case
void test_quintic_case(int case_num, quintic_test_case *test_case) {
    printf("─────────────────────────────────────────────────────────────────\n");
    printf("Test Case %d: %s\n", case_num + 1, test_case->description);
    fflush(stdout);  // Force output
    
    // Display polynomial
    printf("Polynomial: ");
    printf("%.1fx⁵", test_case->coeffs[0]);
    for (int i = 1; i < 6; i++) {
        if (test_case->coeffs[i] >= 0) printf(" + ");
        else printf(" ");
        if (i < 5) {
            printf("%.1fx^%d", test_case->coeffs[i], 5-i);
        } else {
            printf("%.1f", test_case->coeffs[i]);  // Constant term (no x)
        }
    }
    printf(" = 0\n");
    
    printf("Expected: %s\n", test_case->expected);
    printf("Mathematical Significance: %s\n", test_case->mathematical_significance);
    printf("─────────────────────────────────────────────────────────────────\n");
    fflush(stdout);  // Force output
    
    // Call assembly function
    printf("🔧 Testing Reference Architecture:\n");
    fflush(stdout);  // Force output
    solve_poly_5_reference(
        test_case->coeffs[0], test_case->coeffs[1], test_case->coeffs[2],
        test_case->coeffs[3], test_case->coeffs[4], test_case->coeffs[5]
    );
    fflush(stdout);  // Force output after assembly call
    
    printf("🚀 Testing Special Cases Solver:\n");
    fflush(stdout);  // Force output
    int roots_found = solve_poly_5_special(
        test_case->coeffs[0], test_case->coeffs[1], test_case->coeffs[2],
        test_case->coeffs[3], test_case->coeffs[4], test_case->coeffs[5]
    );
    printf("Roots found: %d\n", roots_found);
    fflush(stdout);  // Force output
    printf("\n");
}

int main(void) {
    display_quintic_context();
    display_galois_insights();
    
    printf("🧪 Running Quintic Solver Test Suite\n");
    printf("Testing %d quintic polynomial cases...\n\n", num_test_cases);
    
    // Run test cases
    for (int i = 0; i < num_test_cases; i++) {
        test_quintic_case(i, &test_cases[i]);
    }
    
    printf("╔═══════════════════════════════════════════════════════════════╗\n");
    printf("║            Quintic Implementation Development Complete         ║\n");
    printf("║  \"Beyond radicals: where algebra yields to numerical wisdom\"  ║\n");
    printf("╚═══════════════════════════════════════════════════════════════╝\n");
    
    return 0;
}
