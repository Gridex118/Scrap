#include <stdio.h>
#include <stdlib.h>

typedef struct {
    const size_t m;
    int *data;
} SqMatrix;

void populate_matrix(SqMatrix *const matrix) {
    for (size_t i = 0; i < matrix->m; ++i) {
        for (size_t j = 0; j < matrix->m; ++j) {
            printf("Enter element [%zu, %zu]: ", i, j);
            size_t index = (matrix->m * i) + j;
            scanf("%d", &matrix->data[index]);
        }
    }
}

void print_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < matrix->m; ++i) {
        for (size_t j = 0; j < matrix->m; ++j) {
            size_t index = (matrix->m * i) + j;
            printf("%d ", matrix->data[index]);
        }
        putchar('\n');
    }
}

static inline int is_null_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < (matrix->m * matrix->m); ++i) {
        if (matrix->data[i]) return 0;
    }
    return 1;
}

static inline int is_diagonal_element(const size_t i, const size_t j) {
    return (i == j);
}

static inline int is_auxilary_diagonal_element(const size_t i, const size_t j) {
    return (j == i - 1) || (j == i + 1);
}

static inline int is_non_zero_element(const SqMatrix *const matrix, const size_t index) {
    return matrix->data[index];
}

int is_diagonal_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < matrix->m; ++i) {
        for (size_t j = 0; j < matrix->m; ++j) {
            size_t index = (matrix->m * i) + j;
            if (is_non_zero_element(matrix, index)) {
                if (!is_diagonal_element(i, j)) {
                    return 0;
                }
            }
        }
    }
    return 1;
}

int is_tridiagonal_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < matrix->m; ++i) {
        for (size_t j = 0; j < matrix->m; ++j) {
            size_t index = (matrix->m * i) + j;
            if (is_non_zero_element(matrix, index)) {
                if (!(is_diagonal_element(i, j) || is_auxilary_diagonal_element(i, j))) {
                    return 0;
                }
            }
        }
    }
    return 1;
}

int is_upper_triangular_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < matrix->m; ++i) {
        for (size_t j = 0; j < i; ++j) {
            size_t index = (matrix->m * i) + j;
            if (is_non_zero_element(matrix, index)) {
                return 0;
            }
        }
    }
    return 1;
}

int is_lower_triangular_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < matrix->m; ++i) {
        for (size_t j = i + 1; j < matrix->m; ++j) {
            size_t index = (matrix->m * i) + j;
            if (is_non_zero_element(matrix, index)) {
                return 0;
            }
        }
    }
    return 1;
}

void print_irregular_matrix(const SqMatrix *const matrix) {
    for (size_t i = 0; i < (matrix->m * matrix->m); ++i) {
        if (is_non_zero_element(matrix, i)) {
            printf("%d ", matrix->data[i]);
        }
    }
    putchar('\n');
}

int main(void) {
    size_t m;
    printf("Enter matrix (square) dimention: ");
    scanf("%zu", &m);
    SqMatrix matrix = {
        .m = m,
        .data = malloc(m * m * sizeof(int))
    };
    populate_matrix(&matrix);
    print_matrix(&matrix);
    if (is_null_matrix(&matrix)) {
        puts("This is a null matrix");
    } else if (is_diagonal_matrix(&matrix)) {
        puts("This is a diagonal matrix");
    } else if (is_tridiagonal_matrix(&matrix)) {
        puts("This is a tridiagonal matrix");
    } else if (is_lower_triangular_matrix(&matrix)) {
        puts("This is a lower triangular matrix");
    } else if (is_upper_triangular_matrix(&matrix)) {
        puts("This is an upper triangular matrix");
    } else {
        puts("This is an irregular matrix");
        print_irregular_matrix(&matrix);
    }
    free(matrix.data);
    return 0;
}
