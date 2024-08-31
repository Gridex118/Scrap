#include <math.h>
#include <stdio.h>

typedef struct {
    double a;
    double b;
} TwoTouple;

void method_of_bisection(const short precision, TwoTouple *const bounds,
                         double (*const f)(const double), const int iter) {
    double c = (bounds->a + bounds->b) / 2;
    double error = (*f)(c);
    printf("%2d. [%.13lf, %.13lf] : %.13lf -> % .13lf\n", iter, bounds->a, bounds->b, c, error);
    if (fabs(error) > pow(10, -precision)) {
        if (error > 0) {
            bounds->b = c;
        } else {
            bounds->a = c;
        }
        method_of_bisection(precision, bounds, f, iter + 1);
    }
}

double f(const double x) {
    return pow(x, 3) - (4 * x) - 9;
}

int main(void) {
    TwoTouple bounds_init;
    printf("Enter bound start: ");
    scanf("%lf", &bounds_init.a);
    printf("Enter bound end: ");
    scanf("%lf", &bounds_init.b);
    short precision;
    printf("Enter number of decimal places: ");
    scanf("%hd", &precision);
    method_of_bisection(precision, &bounds_init, f, 1);
    return 0;
}
