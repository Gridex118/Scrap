#include <stdio.h>

void get_arr(int *restrict arr, const size_t len) {
    for (size_t i = 0; i < len; ++i) {
        printf("Enter element %zd: ", i);
        scanf("%d", &arr[i]);
    }
}

int main() {
    const size_t len = 5;
    int data[len];
    get_arr(data, len);
    int token;
    printf("Enter token to search: ");
    scanf("%d", &token);
    for (size_t i = 0; i < len; i++) {
        if (data[i] == token) {
            printf("Token found at index %zd\n", i);
            return 0;
        }
    }
    printf("Token not present in array\n");
    return 1;
}
