#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void insert_sort(int *arr, int len){
    for (int i = 1; i < len; ++i) {
        int key = arr[i];
        int j = i - 1;
        while ((arr[j] > key) && (j >= 0)) {
            arr[j+1] = arr[j];
            --j;
        }
        arr[j+1] = key;
    }
}

int main(int argc, char **argv){
    int len = argc - 1;
    int *arr = (int*) malloc(sizeof(int) * len);
    for (int i = 0; i < len; ++i) {
        arr[i] = atoi(argv[i+1]);
    }
    insert_sort(arr, len);
    for (int i = 0; i < len; ++i){
        printf("%d ", arr[i]);
    }
    putchar('\n');
    return 0;
}
