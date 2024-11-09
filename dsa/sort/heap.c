#include "sort.h"

void heapify(int arr[], int n, int i) {
    int largest = i; 
    int l = 2 * i + 1; 
    int r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest]) {
        largest = l;
    }
    if (r < n && arr[r] > arr[largest]) {
        largest = r;
    }
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heap_sort(int arr[], int len) {
    for (int i = len / 2 - 1; i >= 0; i--) {
        heapify(arr, len, i);
    }
    for (int i = len - 1; i > 0; i--) {
        SWAP(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
