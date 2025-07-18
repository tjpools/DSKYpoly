#include <stdio.h>

// Declare the external assembly function
typedef int (*newton_quintic_func)();
extern int newton_quintic();

int main() {
    int result = newton_quintic();
    if (result == 0) {
        // Success: output already printed by assembly
        return 0;
    } else if (result == 1) {
        fprintf(stderr, "[C] Error: Newton-Raphson did not converge.\n");
        return 1;
    } else if (result == 2) {
        fprintf(stderr, "[C] Error: Division by zero encountered.\n");
        return 2;
    } else {
        fprintf(stderr, "[C] Error: Unknown return code %d.\n", result);
        return result;
    }
}
