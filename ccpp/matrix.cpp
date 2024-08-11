#include <iostream>
#include <vector>

namespace matrix {

template <typename T> class Matrix;
template <typename T> std::ostream& operator<<(std::ostream &os, const Matrix<T> &m) noexcept;
template <typename T> Matrix<T> operator+(const Matrix<T> &m1, const Matrix<T> &m2);
template <typename T> Matrix<T> operator*(const Matrix<T> &m1, const Matrix<T> &m2);

template <typename T>
class Matrix {
public:
    Matrix(const size_t rows, const size_t cols);
    T& operator()(const size_t i, const size_t j);
    T operator()(const size_t i, const size_t j) const;
    T& operator[](const size_t i);
    Matrix& operator=(const std::vector<T> arr);
    friend std::ostream& operator<< <>(std::ostream &os, const Matrix<T> &m) noexcept;
    template <typename U>
    friend Matrix<U> operator+(const Matrix<U> &m1, const Matrix<U> &m2);
    template <typename U>
    friend Matrix<U> operator*(const Matrix<U> &m1, const Matrix<U> &m2);
private:
    size_t rows;
    size_t cols;
    std::vector<T> data;
};

template <typename T>
Matrix<T>::Matrix(const size_t rows, const size_t cols)
    : rows(rows),
    cols(cols),
    data(rows * cols)
{

}

template <typename T>
std::ostream& operator<<(std::ostream &os, const Matrix<T> &m) noexcept{
    for (size_t i = 0; i < m.rows; ++i) {
        for (size_t j = 0; j < m.cols; ++j) {
            os << m(i, j) << ' ';
        }
        os << '\n';
    }
    return os;
}

template <typename T>
Matrix<T> operator+(const Matrix<T> &m1, const Matrix<T> &m2) {
    Matrix<T> m3(m1.rows, m1.cols);
    for (size_t i = 0; i < m1.rows; i++) {
        for (size_t j = 0; j < m1.cols; j++) {
            m3(i, j) = m1(i, j) + m2(i, j);
        }
    }
    return m3;
}

template <typename T>
Matrix<T> operator*(const Matrix<T> &m1, const Matrix<T> &m2) {
    Matrix<T> m3(m1.rows, m2.cols);
    for (size_t i = 0; i < m1.rows; ++i) {
        for (size_t j = 0; j < m2.cols; ++j) {
            m3(i, j) = 0;
            for (size_t k = 0; k < m1.cols; ++k) {
                m3(i, j) += m1(i, k) * m2(k, j);
            }
        }
    }
    return m3;
}

template <typename T>
Matrix<T>& Matrix<T>::operator=(const std::vector<T> arr) {
    for (size_t i = 0; i < (rows * cols); ++i) {
        data[i] = arr.at(i);
    }
    return *this;
}

template <typename T>
T& Matrix<T>::operator()(const size_t i, const size_t j) {
    return data[(i * cols) + j];
}

template <typename T>
T Matrix<T>::operator()(const size_t i, const size_t j) const {
    return data[(i * cols) + j];
}

template <typename T>
T& Matrix<T>::operator[](const size_t i) {
    return data[i];
}

}

int main(void) {
    matrix::Matrix<int> m1(3, 3);
    m1 = {
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    };
    matrix::Matrix<int> m2(3, 3);
    m2 = {
        1, 0, 0,
        0, 1, 0,
        0, 0, 1
    };
    matrix::Matrix m3 = m1 * m2;
    std::cout << m3;
    return 0;
}
