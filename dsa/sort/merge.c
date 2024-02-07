#include "sort.h"
#include <string.h>

void merge(int b[], int begin, int middle, int end, int a[]) {
    int i = begin, j = middle;
    for (int k = begin; k < end; k++) {
        if ((i < middle) && (j >= end || a[i] <= a[j])) {
            b[k] = a[i++];
        } else {
            b[k] = a[j++];
        }
    }
}

// The end index is not inclusive
void split_merge(int b[], int begin, int end, int a[]) {
    if ((end - begin) <= 1) return;
    int middle = (int)((end + begin)/2);
    split_merge(a, begin, middle, b);
    split_merge(a, middle, end, b);
    merge(b, begin, middle, end, a);
}

void merge_sort(int arr[], int len) {
    int aux_arr[len];
    memcpy(aux_arr, arr, len * sizeof(int));
    // Split the array, recursively, into halves and sort each of them
    split_merge(arr, 0, len, aux_arr);
}
