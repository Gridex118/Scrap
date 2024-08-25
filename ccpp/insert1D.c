#include <stdio.h>

typedef struct {
    const size_t capacity;
    size_t len;
    int *data;
} Array;

void print_array(const Array *const arr) {
    printf("The array: ");
    for (size_t i = 0; i < arr->len; ++i) {
        printf("%d ", arr->data[i]);
    }
    putchar('\n');
}

void populate_array(Array *const arr) {
    for (size_t i = 0; i < arr->len; ++i) {
        printf("Enter element %zu: ", i);
        scanf("%d", &arr->data[i]);
    }
}

int insert(Array *const arr, const size_t at, const int val) {
    if (arr->len >= arr->capacity) {
        fprintf(stderr, "Can not add any more elements\n");
        return -1;
    }
    for (size_t i = arr->len; i > at; --i) {
        arr->data[i] = arr->data[i - 1];
    }
    arr->data[at] = val;
    ++arr->len;
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
    print_array(&arr);
    int val;
    printf("Enter element to insert: ");
    scanf("%d", &val);
    size_t at;
    printf("Insert at index: ");
    scanf("%zu", &at);
    if (insert(&arr, at, val) != 0) return -1;
    puts("The new array is: ");
    print_array(&arr);
    return 0;
}
