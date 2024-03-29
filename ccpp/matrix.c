#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define INPUT_BUFFER_SIZE 128

void matrix_add(int rows, int cols, int matrix_a[rows][cols], int matrix_b[rows][cols], int matrix_c[rows][cols]) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j)
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j];
    }
}

void matrix_multipy(int rows_a, int cols_a, int cols_b, int matrix_a[rows_a][cols_a], int matrix_b[cols_a][cols_b], int matrix_c[rows_a][cols_b]) {
    for (int i = 0; i < rows_a; ++i) {
        for (int j = 0; j < cols_b; ++j) {
            matrix_c[i][j] = 0;
            for (int k = 0; k < cols_a; ++k)
                matrix_c[i][j] += (matrix_a[i][k] * matrix_b[k][j]);
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
        for (int j = 0; j < cols; ++j)
            printf("%4d ", matrix[i][j]);
        putchar('\n');
    }
}

static inline void print_row_prompt(int row, int cols) {
    printf("Enter %d row elements", row);
    // Display required indices
    for (int i = 0; i < cols; ++i)
        printf("[%d %d] ", row, i);
    printf("\n>> ");
}

static inline int parse_row_input(char *buf, int row, int cols, int matrix[][cols]) {
    buf[strcspn(buf, "\n")] = '\0';
    char *split = strtok(buf, " ");
    char *end;
    int j = 0;
    while (split) {
        if (j >= cols) {
            fputs("WARNING: Input has more elements than required; turncating\n", stderr);
            break;
        }
        matrix[row][j++] = (int) strtol(split, &end, 10);
        if (end == split) {
            fputs("ERROR: not a valid integer input\n", stderr);
            return -1;
        }
        split = strtok(NULL, " ");
    }
    return j;
}

int matrix_input(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; ++i) {
        print_row_prompt(i, cols);
        char buf[INPUT_BUFFER_SIZE];
        if (fgets(buf, INPUT_BUFFER_SIZE, stdin) == NULL) {
            fputs("ERROR reading input\n", stderr);
            return -1;
        }
        int elements_read = parse_row_input(buf, i, cols, matrix);
        if (elements_read == -1) return -1;
        if (elements_read < cols) {
            fputs("ERROR: Input has less elements than required\n", stderr);
            return -1;
        }
    }
    return 0;
}

void matrix_add_33(int matrix_a[3][3], int matrix_b[3][3], int matrix_c[3][3]) {
    matrix_add(3, 3, matrix_a, matrix_b, matrix_c);
}

void matrix_multipy_33(int matrix_a[3][3], int matrix_b[3][3], int matrix_c[3][3]) {
    matrix_multipy(3, 3, 3, matrix_a, matrix_b, matrix_c);
}

void matrix_transpose_33(int matrix[3][3]) {
    matrix_transpose(3, 3, matrix);
}

void matrix_print_33(int matrix[3][3]) {
    matrix_print(3, 3, matrix);
}

int matrix_input_33(int matrix[3][3]) {
    return matrix_input(3, 3, matrix);
}

int main(void) {
    int matrix_a[3][3] = {{3, 1, 5}, {2, 2, 9}, {7, 3, 4}};
    int matrix_b[3][3] = {{3, 1, 5}, {2, 2, 9}, {7, 3, 4}};
    int matrix_c[3][3];
    matrix_multipy_33(matrix_a, matrix_b, matrix_c);
    putchar('\n');
    matrix_print_33(matrix_c);
    return 0;
}
