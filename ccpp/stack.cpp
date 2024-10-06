#include <iostream>
#include <array>

#define STACK_MAX 100

class Stack {
private:
    size_t size_;
    size_t SP_{0};
    std::array<int, STACK_MAX> data_{0};
public:
    Stack(const size_t size): size_(size) {  };
    Stack(void): size_(10) {  };
    void push(const int element);
    void pop(void);
    friend void display_stack(const Stack *const stack);
};

void Stack::push(const int element) {
    if (SP_ < size_ - 1) {
        data_[SP_++] = element;
    } else {
        std::cout << "Overfow!\n";
    }
}

void Stack::pop(void) {
    if (SP_ > 0) {
        std::cout << "Popping " << data_[--SP_] << '\n';
    } else {
        std::cout << "Underflow!\n";
    }
}

void display_stack(const Stack *const stack) {
    for (size_t i = 0; i < stack->SP_; i++) {
        std::cout << stack->data_.at(i) << ' ';
    }
    std::cout << '\n';
}

int main(void) {
    Stack stack;
    for (size_t i = 0; i < 5; i++) {
        stack.push(i + 1);
    }
    display_stack(&stack);
    stack.pop();
    display_stack(&stack);
    return 0;
}
