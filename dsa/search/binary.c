#include <stdio.h>

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
    int data[] = {2, 4, 5, 12, 33, 43, 55, 73};
    int length = (sizeof data / sizeof data[0]);
    int token = 13;
    int index = binary_search(token, data, 0, length - 1);
    printf("Token found at index %d\n", index);

    return 0;
}
