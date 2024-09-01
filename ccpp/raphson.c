#include <stdio.h>
#include <math.h>

double f(const double x) {
    return pow(x, 3) - (4 * x) - 9;
}

double f_prime(const double x) {
    return (3 * pow(x, 2)) - 4;
}

void newton_raphson_method(const unsigned short precision, const double x_n,
                           double (*f)(const double), double (*f_prime)(const double)) {
    double x_n1 = x_n - (*f)(x_n)/(*f_prime)(x_n);
    double error = f(x_n1);
    printf("%.13lf -> %.13lf\n", x_n1, error);
    if (fabs(error) < pow(10, -precision)) {
        printf("Root is approximately %.13lf\n", x_n1);
    } else {
        newton_raphson_method(precision, x_n1, f, f_prime);
    }
}

int main(void) {
    unsigned short precision;
    printf("Enter precision: ");
    scanf("%hu", &precision);
    double initial_guess;
    printf("Enter initial guess: ");
    scanf("%lf", &initial_guess);
    newton_raphson_method(precision, initial_guess, &f, &f_prime);
    return 0;
}
