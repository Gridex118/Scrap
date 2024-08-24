#include <stdio.h>
#include <stdlib.h>

void traverse_arr(int *const restrict arr, const size_t len) {
    printf("The array: ");
    for (size_t i = 0; i < len; ++i) {
        printf("%d ", arr[i]);
    }
    putchar('\n');
}

void populate_array(int *const restrict arr, const size_t len) {
    for (size_t i = 0; i < len; ++i) {
        printf("Enter element %zu: ", i);
        scanf("%d", arr + i);
    }
}

int main(void) {
    size_t len;
    printf("Enter number of elements in array: ");
    scanf("%zu", &len);
    int *arr = malloc(len * sizeof(int));
    populate_array(arr, len);
    putchar('\n');
    traverse_arr(arr, len);
    return 0;
}
