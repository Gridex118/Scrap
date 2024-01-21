#include <iostream>

template<typename T, size_t N>
bool search(T (&arr)[N], T key) {
    for (size_t i=0; i < N; i++) {
        if (arr[i] == key)
            return true;
    }
    return false;
}

int main() {
    int arr[] = {1, 23, 34, 32, 2, 3, 4, 5, 8, 6};
    int key;
    std::cout << "Enter the element to search for: ";
    std::cin >> key;
    if (search(arr, key))
        std::cout << "Key is present\n";
    else
        std::cout << "Key is absent\n";
    return 0;
}
