/*
 * DSKYpoly-4: Quartic Polynomial Solver using Ferrari's Method
 * 
 * This C interface provides a symbolic bridge between human mathematical
 * intuition and the mechanical precision of Ferrari's algorithm implemented
 * in x86-64 assembly.
 * 
 * Ferrari's Method (1522-1565):
 * - Student of Cardano, extended cubic solutions to quartic
 * - Transforms quartic → resolvent cubic → Cardano's method → quartic roots
 * - Beautiful recursive mathematical structure
 * 
 * Input: Quartic polynomial ax⁴ + bx³ + cx² + dx + e = 0
 * Output: Up to 4 roots (real or complex)
 */

#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <string.h>

// External assembly functions
extern void solve_poly_4_reference(double a, double b, double c, double d, double e);
extern void solve_poly_4_production(double a, double b, double c, double d, double e);

// Test cases for Ferrari's method validation
typedef struct {
    double a, b, c, d, e;
    const char* description;
    const char* expected_roots;
} QuarticTestCase;

// Collection of test cases covering different quartic types
QuarticTestCase test_cases[] = {
    // Biquadratic (no odd powers) - perfect for Ferrari method
    {1.0, 0.0, -10.0, 0.0, 9.0, 
     "Biquadratic", "x = ±1, ±3"},
    
    // Depressed quartic (no cubic term)
    {1.0, 0.0, -5.0, 0.0, 6.0, 
     "Depressed quartic", "x = ±1, ±√6"},
    
    // General quartic
    {1.0, -4.0, 6.0, -4.0, 1.0, 
     "General quartic", "x = 1 (multiplicity 4)"},
    
    // Quartic with complex roots
    {1.0, 0.0, 1.0, 0.0, 1.0, 
     "Complex roots", "x = ±i, ±1/i"},
    
    // Ferrari's historical example (approximate)
    {1.0, -2.0, -1.0, 2.0, 1.0, 
     "Ferrari's example", "Mixed real/complex"}
};

void print_header() {
    printf("╔═══════════════════════════════════════════════════════════════╗\n");
    printf("║                    DSKYpoly-4 Quartic Solver                  ║\n");
    printf("║                    Ferrari's Method (1522-1565)               ║\n");
    printf("╠═══════════════════════════════════════════════════════════════╣\n");
    printf("║ Transforms: ax⁴ + bx³ + cx² + dx + e = 0                     ║\n");
    printf("║ Method: Quartic → Resolvent Cubic → Cardano's → Roots        ║\n");
    printf("║ Implementation: x86-64 Assembly with SSE floating-point      ║\n");
    printf("╚═══════════════════════════════════════════════════════════════╝\n");
    printf("\n");
}

void print_test_case_header(int test_num, QuarticTestCase* test) {
    printf("─────────────────────────────────────────────────────────────────\n");
    printf("Test Case %d: %s\n", test_num, test->description);
    printf("Polynomial: %.1fx⁴ + %.1fx³ + %.1fx² + %.1fx + %.1f = 0\n", 
           test->a, test->b, test->c, test->d, test->e);
    printf("Expected: %s\n", test->expected_roots);
    printf("─────────────────────────────────────────────────────────────────\n");
}

void run_interactive_mode() {
    double a, b, c, d, e;
    char choice;
    
    printf("🎯 Interactive Quartic Solver\n");
    printf("Enter coefficients for ax⁴ + bx³ + cx² + dx + e = 0\n\n");
    
    do {
        printf("Enter coefficient a (quartic): ");
        scanf("%lf", &a);
        
        if (a == 0.0) {
            printf("Error: Leading coefficient cannot be zero for quartic equation.\n");
            continue;
        }
        
        printf("Enter coefficient b (cubic): ");
        scanf("%lf", &b);
        
        printf("Enter coefficient c (quadratic): ");
        scanf("%lf", &c);
        
        printf("Enter coefficient d (linear): ");
        scanf("%lf", &d);
        
        printf("Enter coefficient e (constant): ");
        scanf("%lf", &e);
        
        printf("\n🔧 Reference Architecture Result:\n");
        solve_poly_4_reference(a, b, c, d, e);
        
        printf("\n🚀 Production Implementation Result:\n");
        solve_poly_4_production(a, b, c, d, e);
        
        printf("\nSolve another quartic? (y/n): ");
        scanf(" %c", &choice);
        printf("\n");
        
    } while (choice == 'y' || choice == 'Y');
}

void run_test_suite() {
    int num_tests = sizeof(test_cases) / sizeof(QuarticTestCase);
    
    printf("🧪 Running Ferrari Method Test Suite\n");
    printf("Testing %d quartic polynomial cases...\n\n", num_tests);
    
    for (int i = 0; i < num_tests; i++) {
        QuarticTestCase* test = &test_cases[i];
        
        print_test_case_header(i + 1, test);
        
        printf("🔧 Testing Reference Architecture:\n");
        // Call the reference implementation (stable architecture)
        solve_poly_4_reference(test->a, test->b, test->c, test->d, test->e);
        
        printf("\n🚀 Testing Production Implementation:\n");
        // Call the production implementation (full Ferrari mathematics)
        solve_poly_4_production(test->a, test->b, test->c, test->d, test->e);
        
        printf("\n");
    }
}

void print_ferrari_info() {
    printf("📜 Historical Context: Ferrari's Method\n");
    printf("═══════════════════════════════════════\n");
    printf("• Ludovico Ferrari (1522-1565)\n");
    printf("• Student of Gerolamo Cardano\n");
    printf("• Discovered general solution to quartic equations\n");
    printf("• Method: Reduce quartic to resolvent cubic\n");
    printf("• Revolutionary: First general algebraic solution beyond cubic\n");
    printf("• Computational beauty: Recursive use of Cardano's method\n\n");
    
    printf("🔬 Algorithm Overview:\n");
    printf("═══════════════════════\n");
    printf("1. Depress quartic: Remove cubic term by substitution\n");
    printf("2. Resolvent cubic: Transform to 8t³ + 8pt² + (2p² - 8r)t - q² = 0\n");
    printf("3. Cardano's method: Solve the resolvent cubic\n");
    printf("4. Root extraction: Use cubic solution to find quartic roots\n");
    printf("5. Back-substitution: Transform back to original variable\n\n");
}

int main(int argc, char* argv[]) {
    print_header();
    
    if (argc > 1) {
        if (strcmp(argv[1], "--test") == 0) {
            run_test_suite();
        } else if (strcmp(argv[1], "--info") == 0) {
            print_ferrari_info();
        } else if (strcmp(argv[1], "--interactive") == 0) {
            run_interactive_mode();
        } else {
            printf("Usage: %s [--test|--info|--interactive]\n", argv[0]);
            printf("  --test        Run test suite\n");
            printf("  --info        Show Ferrari method information\n");
            printf("  --interactive Enter interactive mode\n");
            printf("  (no args)     Run default test suite\n");
        }
    } else {
        // Default: run test suite
        run_test_suite();
    }
    
    printf("╔═══════════════════════════════════════════════════════════════╗\n");
    printf("║              Ferrari's Method Implementation Complete          ║\n");
    printf("║     \"The quartic yields its secrets through cubic wisdom\"     ║\n");
    printf("╚═══════════════════════════════════════════════════════════════╝\n");
    
    return 0;
}

/*
 * Notes on Ferrari's Method Implementation:
 * 
 * Mathematical Elegance:
 * - Transforms 4th degree problem into 3rd degree problem
 * - Recursive application of already-solved cubic case
 * - Demonstrates the interconnectedness of polynomial solutions
 * 
 * Computational Structure:
 * - Systematic coefficient transformations
 * - Modular approach: each step has clear mathematical purpose
 * - Assembly implementation leverages SSE for parallel computation
 * 
 * Historical Significance:
 * - Last general algebraic solution for polynomial equations
 * - Abel-Ruffini theorem proves no general solution for degree ≥ 5
 * - Ferrari's method represents peak of classical algebraic methods
 * 
 * This implementation bridges pure mathematics and mechanical computation,
 * embodying the philosophical coherence described in the grammar directory.
 */
