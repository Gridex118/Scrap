#ifndef SORT_H
#define SORT_H

#include <stdio.h>

#define SWAP(A,B) { \
    int tmp = A; \
    A = B; \
    B = tmp; \
}

void bubble_sort(int arr[], int len);
void insert_sort(int arr[], int len);
void merge_sort(int arr[], int len);

#endif
