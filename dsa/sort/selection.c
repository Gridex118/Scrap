#include "sort.h"

void selection_sort(int arr[], int len) {
    for (int i = 0; i < len - 1; i++) {
        int i_min = i;
        for (int j = i + 1; j < len; ++j) {
            if (arr[j] < arr[i_min]) {
                i_min = j;
            }
        }
        SWAP(arr[i], arr[i_min]);
    }
}
