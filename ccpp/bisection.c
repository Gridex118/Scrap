#include <stdio.h>
#include <math.h>

typedef struct {
    double a;
    double b;
} TwoTouple;

void method_of_bisection(TwoTouple *const bounds, double (*const f)(const double)) {
    static int iter = 1;
    double c = (bounds->a + bounds->b) / 2;
    double error = (*f)(c);
    printf("%d. [%.13lf, %.13lf] -> %.13lf\n", iter, bounds->a, bounds->b, error);
    if (fabs(error) > 0.001) {
        if (error > 0) {
            bounds->b = c;
        } else {
            bounds->a = c;
        }
        ++iter;
        method_of_bisection(bounds, f);
    }
}

double f(const double x) {
    return pow(x, 3) - (4 * x) - 9;
}

double g(const double x) {
    return (x * log10(x)) - 1.2;
}

int main(void) {
    TwoTouple bounds_init = {
        .a = 2.7, .b = 2.8
    };
    method_of_bisection(&bounds_init, g);
    return 0;
}
