#include <stdio.h>
#include <stdlib.h>

typedef struct {
    size_t m;
    size_t n;
    int *data;
} Array2D;

void init_arr2d(Array2D *const arr, const size_t m, const size_t n) {
    arr->m = m;
    arr->n = n;
    arr->data = malloc(m * n * sizeof(int));
}

void populate_arr2d(Array2D *const arr) {
    for (size_t i = 0; i < arr->m; ++i) {
        for (size_t j = 0; j < arr->n; ++j) {
            size_t index = (arr->n * i) + j;
            printf("Enter element [%zu, %zu]: ", i, j);
            scanf("%d", &arr->data[index]);
        }
    }
}

void print_arr2d(Array2D *const arr) {
    for (size_t i = 0; i < arr->m; ++i) {
        for (size_t j = 0; j < arr->n; ++j) {
            size_t index = (arr->n * i) + j;
            printf("%d ", arr->data[index]);
        }
        putchar('\n');
    }
}

void mult_arr2d(Array2D *const arr1, Array2D *const arr2, Array2D *const arr_prod) {
    init_arr2d(arr_prod, arr1->m, arr2->n);
    for (size_t i = 0; i < arr_prod->m; ++i) {
        for (size_t j = 0; j < arr_prod->n; ++j) {
            size_t index = (arr_prod->n * i) + j;
            arr_prod->data[index] = 0;
            for (size_t k = 0; k < arr1->n; ++k) {
                arr_prod->data[index] += arr1->data[arr1->n * i + k] * arr2->data[arr2->n * k + j];
            }
        }
    }
}

int main(void) {
    puts("First array:");
    size_t m1;
    printf("Enter number of rows: ");
    scanf("%zu", &m1);
    size_t n1;
    printf("Enter number of columns (This will determine the number of rows in the second array): ");
    scanf("%zu", &n1);
    Array2D arr1;
    init_arr2d(&arr1, m1, n1);
    populate_arr2d(&arr1);
    puts("\nSecond array:");
    size_t n2;
    printf("Enter number of columns: ");
    scanf("%zu", &n2);
    Array2D arr2;
    init_arr2d(&arr2, n1, n2);
    populate_arr2d(&arr2);
    Array2D arr3;
    mult_arr2d(&arr1, &arr2, &arr3);
    puts("\nMatrix Product");
    print_arr2d(&arr3);
    return 0;
}
