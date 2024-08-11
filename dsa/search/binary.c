#include <stdio.h>

void get_arr(int *restrict arr, const size_t len) {
    for (size_t i = 0; i < len; ++i) {
        printf("Enter element %zd: ", i);
        scanf("%d", &arr[i]);
    }
}

int binary_search(int token, int array[], int low, int high) {
    if (low > high) return -1;
    int mid = (int)(low + (high - low)/2);
    if (token == array[mid]) {
        return mid;
    } else if (token < array[mid]) {
        return binary_search(token, array, low, mid - 1);
    } else {
        return binary_search(token, array, mid + 1, high);
    }
}

int main(void){
    const int length = 5;
    int data[length];
    get_arr(data, length);
    int token;
    printf("Enter token to search: ");
    scanf("%d", &token);
    int index = binary_search(token, data, 0, length - 1);
    printf("Token found at index %d\n", index);

    return 0;
}
