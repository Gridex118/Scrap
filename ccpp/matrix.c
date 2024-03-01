#include <stdio.h>

void matrix_add(int rows, int cols, int matrix_a[rows][cols], int matrix_b[rows][cols], int matrix_c[rows][cols]) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j];
        }
    }
}

void matrix_transpose(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; ++i) {
        for (int j = i; j < cols; ++j) {
            int tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }
}

void matrix_print(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            printf("%d ", matrix[i][j]);
        }
        putchar('\n');
    }
}

void matrix_add_33(int matrix_a[3][3], int matrix_b[3][3], int matrix_c[3][3]) {
    matrix_add(3, 3, matrix_a, matrix_b, matrix_c);
}

void matrix_transpose_33(int matrix[3][3]) {
    matrix_transpose(3, 3, matrix);
}

void matrix_print_33(int matrix[3][3]) {
    matrix_print(3, 3, matrix);
}

int main(void) {
    int matrix_a[3][3] = {{2, 3, 3}, {2, 1, 1}, {1, 3, 4}};
    int matrix_b[3][3] = {{3, 1, 5}, {2, 2, 9}, {7, 3, 4}};
    int matrix_c[3][3];
    matrix_add_33(matrix_a, matrix_b, matrix_c);
    matrix_transpose_33(matrix_c);
    matrix_print_33(matrix_c);
    return 0;
}
