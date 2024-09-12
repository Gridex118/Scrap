#include <stdio.h>
#include <stdlib.h>

typedef struct {
    const size_t n;
    double *x;
    double *y;
} DataTable;

double lagrange_interpolation_method(const DataTable *const table, const double interpol_x) {
    double interpol_y = 0;
    for (size_t i = 0; i < table->n; ++i) {
        double term = 1;
        for (size_t j = 0; j < table->n; ++j) {
            if (i != j) {
                term *= (interpol_x - table->x[j]) / (table->x[i] - table->x[j]);
            }
        }
        interpol_y += term * table->y[i];
    }
    return interpol_y;
}

void populate_table(DataTable *const table) {
    for (size_t i = 0; i < table->n; ++i) {
        printf("Enter data input (x y): ");
        scanf("%lf %lf", &table->x[i], &table->y[i]);
    }
}

void display_table(const DataTable *const table) {
    for (size_t i = 0; i < table->n; ++i) {
        printf("%lf\t%lf\n", table->x[i], table->y[i]);
    }
}

int main(void) {
    size_t n;
    printf("Enter number of data inputs: ");
    scanf("%zu", &n);
    DataTable table = {
        .n = n,
        .x = malloc(sizeof(double) * n),
        .y = malloc(sizeof(double) * n)
    };
    populate_table(&table);
    display_table(&table);
    double interpol_x;
    printf("Enter point of interpolation: ");
    scanf("%lf", &interpol_x);
    double interpol_y = lagrange_interpolation_method(&table, interpol_x);
    printf("At x = %lf, y = %lf\n", interpol_x, interpol_y);
    return 0;
}
