#include <stdio.h>

typedef struct {
    const size_t capacity;
    size_t len;
    int *data;
} Array;

void print_arr(const Array *const restrict arr) {
    printf("The array: ");
    for (size_t i = 0; i < arr->len; ++i) {
        printf("%d ", arr->data[i]);
    }
    putchar('\n');
}

void populate_array(Array *const restrict arr) {
    for (size_t i = 0; i < arr->len; ++i) {
        printf("Enter element %zu: ", i);
        scanf("%d", &arr->data[i]);
    }
}

int delete(Array *const restrict arr, const size_t at) {
    if (arr->len == 0) {
        fprintf(stderr, "Can not delete more elements\n");
        return -1;
    }
    for (size_t i = at; i < arr->len; ++i) {
        arr->data[i] = arr->data[i + 1];
    }
    --arr->len;
    return 0;
}

int main(void) {
    Array arr = {
        .capacity = 15
    };
    int data[arr.capacity];
    arr.data = data;
    printf("Enter number of elements in array: ");
    scanf("%zu", &arr.len);
    if (arr.len >= arr.capacity) {
        fprintf(stderr, "A maximum of %zu elements is allowed here\n", arr.capacity - 1);
        return -1;
    }
    populate_array(&arr);
    print_arr(&arr);
    size_t at;
    printf("Insert at index: ");
    scanf("%zu", &at);
    if (delete(&arr, at) != 0) return -1;
    puts("The new array is: ");
    print_arr(&arr);
    return 0;
}
