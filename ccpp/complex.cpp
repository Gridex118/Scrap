#include <iostream>

class Complex {
private:
    int x_;
    int y_;
public:
    Complex(const int x, const int y): x_(x), y_(y) {  };
    Complex(const int x): x_(x), y_(0) {  };
    friend std::ostream& operator<<(std::ostream& os, const Complex &c);
    friend std::istream& operator>>(std::istream& is, Complex &c);
};

std::ostream& operator<<(std::ostream& os, const Complex &c) {
    os << '(' << c.x_ << ", " << c.y_ << ")\n";
    return os;
}

std::istream& operator>>(std::istream& is, Complex &c) {
    std::cout << "X: ";
    is >> c.x_;
    std::cout << "Y: ";
    is >> c.y_;
    return is;
}

int main(void) {
    Complex c1(10);
    std::cout << c1;
    std::cin >> c1;
    std::cout << c1;
    return 0;
}
