#include "sort.h"

#define SORT merge_sort

static inline void print_array(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d", arr[i]);
        if (i != len - 1) printf(", ");
    }
    putchar('\n');
}

int main(void) {
    int data[] = {3, 44, 32, 1, 23, 4, 33, 20, 43};
    int length = (sizeof data / sizeof data[0]);
    printf("Original Array: "); print_array(data, length);
    SORT(data, length);
    printf("Sorted Array: "); print_array(data, length);
    return 0;
}
