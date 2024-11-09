#include "sort.h"

static inline void print_array(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d", arr[i]);
        if (i != len - 1) printf(", ");
    }
    putchar('\n');
}

int main(void) {
    int data[] = { 53, 99, 18, 85, 13, 89, 41, 19, 85, 40 };
    int length = (sizeof data / sizeof data[0]);
    printf("Original Array: "); print_array(data, length);
#ifdef SORT
    SORT(data, length);
#endif /* ifdef SORT */
    printf("Sorted Array: "); print_array(data, length);
    return 0;
}
