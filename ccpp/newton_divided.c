#include <stdio.h>
#include <stdlib.h>

typedef struct {
    const size_t n;
    double *x;
    double *y;
} DataTable;

void generate_difference_table(DataTable *const table) {
    for (size_t j = 1; j < table->n; ++j) {
        for (size_t i = j; i < table->n; ++i) {
            double y_n = table->y[i * table->n + j - 1];
            double y_n1 = table->y[(i - 1) * table->n + j - 1];
            double x_n = table->x[i];
            double x_nj = table->x[i - j];
            table->y[i * table->n + j] = (y_n - y_n1)/(x_n - x_nj);
        }
    }
}

void populate_table(DataTable *const table) {
    for (size_t i = 0; i < table->n; ++i) {
        printf("Enter data entry index %zu (x y): ", i);
        scanf("%lf %lf", &table->x[i], &table->y[i * table->n]);
    }
    generate_difference_table(table);
}

void print_table(const DataTable *const table) {
    for (size_t i = 0; i < table->n; ++i) {
        printf("% lf\t", table->x[i]);
        for (size_t j = 0; j < table->n; ++j) {
            printf("% lf\t", table->y[i * table->n + j]);
        }
        putchar('\n');
    }
}

double newton_divided_difference(const DataTable *const table, const double interpol_x) {
    double interpol_y = table->y[0];
    for (size_t j = 1; j < table->n; ++j) {
        double term = 1;
        for (size_t i = 0; i < j; ++i) {
            term *= (interpol_x - table->x[i]);
        }
        interpol_y += term * table->y[j * table->n + j];
    }
    return interpol_y;
}

int main(void) {
    size_t n;
    printf("Enter number of data entries: ");
    scanf("%zu", &n);
    DataTable table = {
        .n = n,
        .x = calloc(n, sizeof(double)),
        .y = calloc(n * n, sizeof(double))
    };
    populate_table(&table);
    print_table(&table);
    double interpol_x;
    printf("Enter point to interpolate: ");
    scanf("%lf", &interpol_x);
    double interpol_y = newton_divided_difference(&table, interpol_x);
    printf("At %lf, y = %lf\n", interpol_x, interpol_y);
    return 0;
}
