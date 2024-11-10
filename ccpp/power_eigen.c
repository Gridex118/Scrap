#include <stdio.h>

#define MAX_ITERATIONS 5

void populate_matrix(float matrix[2][2]) {
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%f", &matrix[i][j]);
        }
    }
}

void print_matrix(float matrix[2][2]) {
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            printf("%f ", matrix[i][j]);
        }
        putchar('\n');
    }
}

void helper_matrix_multiply(float m1[2][2], float m2[2], float result[2]) {
    for (int i = 0; i < 2; ++i) {
        result[i] = (m2[0] * m1[i][0]) + (m2[1] * m1[i][1]);
    }
}

static inline float helper_max(float pair[2]) {
    return (pair[0] > pair[1])? pair[0] : pair[1];
}

void set_eigen_vector_from_intermediate(float intermediate_matrix[2], float eigen_value, float eigen_vector[2]) {
    for (int i = 0; i < 2; ++i)
        eigen_vector[i] = intermediate_matrix[i] / eigen_value;
}

void power_method(float matrix[2][2], float eigen_vector[2], int iteration) {
    float eigen_value_this_iteration;
    float eigen_vector_this_iteration[2];
    float interemediate_product_matrix[2];
    helper_matrix_multiply(matrix, eigen_vector, interemediate_product_matrix);
    eigen_value_this_iteration = helper_max(interemediate_product_matrix);
    set_eigen_vector_from_intermediate(
        interemediate_product_matrix,
        eigen_value_this_iteration,
        eigen_vector_this_iteration
    );
    printf("Eigen value %d: %f\n", iteration, eigen_value_this_iteration);
    printf("Eigen vector %d:\n", iteration);
    printf("\t%-f\n\t%-f\n", eigen_vector_this_iteration[0], eigen_vector_this_iteration[1]);
    if (iteration != MAX_ITERATIONS)
        power_method(matrix, eigen_vector_this_iteration, iteration + 1);
}

int main(void) {
    float matrix[2][2];
    populate_matrix(matrix);
    float eigen_vector_initial[2];
    printf("Enter first approximation of eigen vector (x y): ");
    scanf("%f %f", &eigen_vector_initial[0], &eigen_vector_initial[1]);
    power_method(matrix, eigen_vector_initial, 1);
    return 0;
}
