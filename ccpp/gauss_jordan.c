#include <stdio.h>
#include <stdlib.h>

void populate_matrix(double *matrix, const int dimension) {
    for (int i = 0; i < dimension; ++i) {
	for (int j = 0; j < dimension; ++j) {
	    printf("Enter element (%d,%d): ", i, j);
	    scanf("%lf", &matrix[i*2*dimension + j]);
	}
    }
    // Filling the identity side of the augmented matrix
    for (int i = 0; i < dimension; ++i) {
	for (int j = dimension; j < 2*dimension; ++j) {
	    matrix[i*2*dimension + j] = ((i == (j - dimension))? 1 : 0);
	}
    }
}

void perform_inversion(double *matrix, const int dimension) {
    for (int i = 0; i < dimension; ++i) {
	for (int k = 0; k < dimension; ++k) {
	    if (i != k) {
		double multiplier = (matrix[k*2*dimension + i] / matrix[i*2*dimension + i]);
		for (int j = 0; j < 2*dimension; ++j) {
		    matrix[k*2*dimension + j] -= multiplier * matrix[i*2*dimension + j];
		}
	    }
	}
    }
    // Normalize the diagonal elements
    for (int i = 0; i < dimension; ++i) {
	double divider = matrix[i*2*dimension + i];
	for (int j = 0; j < 2*dimension; ++j) {
	    matrix[i*2*dimension + j] /= divider;
	}
    }
}

void print_matrix(double *matrix, const int dimension) {
    for (int i = 0; i < dimension; ++i) {
	for (int j = 0; j < 2*dimension; ++j) {
	    printf("% .3lf ", matrix[i*2*dimension + j]);
	    if (j == dimension - 1) putchar('\t');
	}
	putchar('\n');
    }
}

int main(void) {
    int dimension;
    printf("Enter the dimension of the matrix: ");
    scanf("%d", &dimension);
    // Double the columns, for storing the data from the augmented matrix
    double *matrix = malloc(sizeof(double) * dimension * (2 * dimension));
    populate_matrix(matrix, dimension);
    perform_inversion(matrix, dimension);
    puts("The result of inversion is:");
    print_matrix(matrix, dimension);
    return 0;
}
