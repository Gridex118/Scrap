#include "sort.h"

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
