#include "stdio.h"
#define LEN(arr) (sizeof(arr)/sizeof(arr[0]))

int main() {
    int data[] = {2, 3, 5, 10, 11, 30, 40, 44, 53};
    int token = 2;
    for (int i = 0; i < LEN(data); i++) {
        if (data[i] == token) {
            printf("Token found at index %d\n", i);
            return 0;
        }
    }
    printf("Token not present in array\n");
    return 1;
}
