#include <stdio.h>
#include <math.h>

typedef struct {
    double a;
    double b;
} Bounds;

void method_of_secant(const unsigned short precision, Bounds *const bounds,
                      double (*f)(const double), const unsigned short iter) {
    double x_n1 = bounds->b;
    double x_n2 = bounds->a;
    double f_x_n1 = (*f)(x_n1);
    double f_x_n2 = (*f)(x_n2);
    double x_n = x_n1 - f_x_n1 * ((x_n1 - x_n2) / (f_x_n1 - f_x_n2));
    double error = (*f)(x_n);
    printf("%2d. [% .13lf, % .13lf] : % .13lf -> % .13lf\n",
           iter, x_n2, x_n1, x_n, error);
    bounds->b = x_n;
    bounds->a =x_n1;
    if (fabs(error) > pow(10, -precision)) {
        method_of_secant(precision, bounds, f, iter + 1);
    }
}

double f(const double x) {
    return x*exp(x) - cos(x);
}

int main(void) {
    Bounds bounds;
    printf("Enter bound init: ");
    scanf("%lf", &bounds.a);
    printf("Enter bound final: ");
    scanf("%lf", &bounds.b);
    unsigned short precision;
    printf("Enter the precision: ");
    scanf("%hud", &precision);
    method_of_secant(precision, &bounds, &f, 1);
    return 0;
}
