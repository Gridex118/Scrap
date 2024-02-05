#include "sort.h"

void insert_sort(int arr[], int len) {
    int i = 1;
    while (i < len) {
        int j = i;
        while ((j > 0) && (arr[j - 1] > arr[j])) {
            SWAP(arr[j - 1], arr[j]);
            --j;
        }
        ++i;
    }
}
