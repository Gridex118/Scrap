#include "stdio.h"

#define SWAP(A,B) { \
    int tmp = A; \
    A = B; \
    B = tmp; \
}

void print_array(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d", arr[i]);
        if (i != len - 1) printf(", ");
    }
    putchar('\n');
}

void bubble_sort(int arr[], int len) {
    int swapped;
    do {
        swapped = 0;
        for (int i = 0; i < len; i++) {
            for (int k = 0; k < len - i - 1; k++) {
                // Sort in ascending order
                if (arr[k] > arr[k + 1]) {
                    SWAP(arr[k], arr[k + 1]);
                    swapped = 1;
                }
            }
        }
    } while (swapped);
}

int main(void){
    int data[] = {3, 44, 32, 1, 23, 4, 33, 20, 43};
    int length = (sizeof data / sizeof data[0]);
    printf("Original Array: "); print_array(data, length);
    bubble_sort(data, length);
    printf("Sorted Array: "); print_array(data, length);

    return 0;
}
