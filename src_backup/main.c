#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// External assembly function
extern void solve_poly_2(double a, double b, double c,
                         double* r1_real, double* r1_imag,
                         double* r2_real, double* r2_imag);

// Persistent state
static double a = 0, b = 0, c = 0;
static double r1_real = 0, r1_imag = 0;
static double r2_real = 0, r2_imag = 0;

// Logging function
void log_event(const char* msg) {
    FILE *log = fopen("DSKYpoly.log", "a");
    if (!log) {
        perror("Log file error");
        return;
    }

    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    fprintf(log, "[%04d-%02d-%02d %02d:%02d:%02d] %s\n",
        t->tm_year + 1900, t->tm_mon + 1, t->tm_mday,
        t->tm_hour, t->tm_min, t->tm_sec, msg);
    fclose(log);
    printf("DSKYpoly: %s\n", msg);
}

// Root display helper
void print_root(const char* label, double real, double imag) {
    if (imag == 0.0)
        printf("%s: %.4f\n", label, real);
    else
        printf("%s: %.4f %c %.4fi\n", label, real, (imag < 0 ? '-' : '+'), fabs(imag));
}

int main() {
    int verb, noun;
    printf("=== DSKYpoly Interface ===\n");

    while (1) {
        printf("\nEnter VERB (action): ");
        scanf("%d", &verb);
        printf("Enter NOUN (target): ");
        scanf("%d", &noun);

        char log_msg[128];
        snprintf(log_msg, sizeof(log_msg), "VERB %02d / NOUN %02d entered.", verb, noun);
        log_event(log_msg);

        if (verb == 10 && noun == 1) {
            printf("Loading quadratic polynomial coefficients...\n");
            log_event("Prompting for coefficients.");
            printf("Enter coefficient a: ");
            scanf("%lf", &a);
            printf("Enter coefficient b: ");
            scanf("%lf", &b);
            printf("Enter coefficient c: ");
            scanf("%lf", &c);
            log_event("Coefficients loaded.");
        } else if (verb == 20 && noun == 1) {
            printf("Solving quadratic polynomial...\n");
            log_event("Calling solver.");
            solve_poly_2(a, b, c, &r1_real, &r1_imag, &r2_real, &r2_imag);
            log_event("Solver completed.");
        } else if (verb == 30 && noun == 1) {
            printf("Displaying the roots:\n");
            log_event("Displaying roots.");
            print_root("Root 1", r1_real, r1_imag);
            print_root("Root 2", r2_real, r2_imag);
        } else if (verb == 99) {
            printf("Exiting DSKYpoly.\n");
            log_event("Program exited.");
            break;
        } else {
            printf("Invalid VERB/NOUN combination.\n");
            log_event("Invalid command.");
        }
    }

    return 0;
}
