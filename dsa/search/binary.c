#include <stdio.h>

void get_arr(int *restrict arr, const size_t len) {
    for (size_t i = 0; i < len; ++i) {
        printf("Enter element %zd: ", i);
        scanf("%d", &arr[i]);
    }
}

int binary_search(const int token, int array[], const int low, const int high) {
    if (low > high) return -1;
    const int MID = (low + high)/2;
    if (token == array[MID]) {
        return MID;
    } else if (token < array[MID]) {
        return binary_search(token, array, low, MID - 1);
    } else {
        return binary_search(token, array, MID + 1, high);
    }
}

int main(void){
    const int LENGTH = 5;
    int data[LENGTH];
    get_arr(data, LENGTH);
    int token;
    printf("Enter token to search: ");
    scanf("%d", &token);
    int index = binary_search(token, data, 0, LENGTH - 1);
    printf("Token found at index %d\n", index);

    return 0;
}
