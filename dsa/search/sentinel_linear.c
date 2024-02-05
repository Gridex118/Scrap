#include <stdio.h>
#define LEN(arr) (sizeof(arr)/sizeof(arr[0]))

int main() {
    int data[] = {2, 3, 5, 10, 11, 34, 43, 44, 50, 0};
    int last_index = LEN(data) - 1;
    int token = 35;
    data[last_index -1] = token;
    int i = 0;
    while (data[i] != token) {
        i++;
    }
    if (i == last_index - 1) {
        printf("Token not found\n");
        return 1;
    } else {
        printf("Token found at index %d\n", i);
        return 0;
    }
}
