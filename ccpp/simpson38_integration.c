#include <stdio.h>

typedef struct {
    double a;
    double b;
    int    n;
} Bounds;

void init_bounds(Bounds *const bounds) {
    printf("Enter integration bounds (a b): ");
    scanf("%lf %lf", &bounds->a, &bounds->b);
    printf("Enter number of steps(n): ");
    scanf("%d", &bounds->n);
}

double simpson38_integration(double f(const double), const Bounds *const bounds) {
    const double step_size = (bounds->b - bounds->a)/bounds->n;
    double integral = f(bounds->a) + f(bounds->b);
    for (int i = 1; i < bounds->n; ++i) {
	double y = f(bounds->a + i*step_size);
	if (i%3 == 0) {
	    integral += 2 * y;
	} else {
	    integral += 3 * y;
	}
    }
    return (3*step_size/8) * integral;
}

double f(const double x) {
    return x*x*x;
}

int main(void) {
    Bounds bounds;
    init_bounds(&bounds);
    printf("The result of the integration is: %lf\n",
           simpson38_integration(f, &bounds));
    return 0;
}
