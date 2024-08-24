#include <stdio.h>
#include <stdlib.h>

typedef struct {
    size_t m;
    size_t n;
    int *data;
} Array2D;

void init_arr2d(Array2D *const restrict arr, const size_t m, const size_t n) {
    arr->m = m;
    arr->n = n;
    arr->data = malloc(m * n * sizeof(int));
}

void populate_arr2d(Array2D *const restrict arr) {
    for (size_t i = 0; i < arr->m; ++i) {
        for (size_t j = 0; j < arr->n; ++j) {
            size_t index = (arr->n * i) + j;
            printf("Enter element [%zu, %zu]: ", i, j);
            scanf("%d", &arr->data[index]);
        }
    }
}

void print_arr2d(Array2D *const restrict arr) {
    for (size_t i = 0; i < arr->m; ++i) {
        for (size_t j = 0; j < arr->n; ++j) {
            size_t index = (arr->n * i) + j;
            printf("%d ", arr->data[index]);
        }
        putchar('\n');
    }
}

void add_arr2d(Array2D *const restrict arr1, Array2D *const restrict arr2, Array2D *const restrict arr_sum) {
    for (size_t i = 0; i < arr_sum->m; ++i) {
        for (size_t j = 0; j < arr_sum->n; ++j) {
            size_t index = (arr_sum->n * i) + j;
            arr_sum->data[index] = arr1->data[index] + arr2->data[index];
        }
    }
}

int main(void) {
    size_t m;
    printf("Enter number of rows: ");
    scanf("%zu", &m);
    size_t n;
    printf("Enter number of columns: ");
    scanf("%zu", &n);
    puts("First array");
    Array2D arr1;
    init_arr2d(&arr1, m, n);
    populate_arr2d(&arr1);
    puts("Second array");
    Array2D arr2;
    init_arr2d(&arr2, m, n);
    populate_arr2d(&arr2);
    Array2D arr3;
    init_arr2d(&arr3, m, n);
    add_arr2d(&arr1, &arr2, &arr3);
    puts("Sum");
    print_arr2d(&arr3);
    return 0;
}
