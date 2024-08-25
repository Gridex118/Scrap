#include <stdio.h>
#include <stdlib.h>

void populate_arr2d(int *const arr, const size_t m, const size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            size_t index = (n * i) + j;
            printf("Enter element [%zu, %zu]: ", i, j);
            scanf("%d", &arr[index]);
        }
    }
}

void print_arr2d(const int *const arr, const size_t m, const size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            size_t index = (n * i) + j;
            printf("%d ", arr[index]);
        }
        putchar('\n');
    }
}

void transpose_arr2d(int *const arr, const size_t m, const size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = i + 1; j < n; ++j) {
            size_t index = (n * i) + j;
            size_t index_trans = (n * j) + i;
            int tmp = arr[index];
            arr[index] = arr[index_trans];
            arr[index_trans] = tmp;
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
    int *arr = malloc(m * n * sizeof(int));
    populate_arr2d(arr, m, n);
    puts("\nOriginal array:");
    print_arr2d(arr, m, n);
    transpose_arr2d(arr, m, n);
    puts("\nArray after transposing:");
    print_arr2d(arr, m, n);
    return 0;
}
