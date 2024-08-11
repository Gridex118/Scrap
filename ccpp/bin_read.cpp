#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <array>
#include <sys/types.h>

inline std::ios::pos_type filesize(std::string file) {
    std::ifstream in(file, std::ios::ate | std::ios::binary);
    return in.tellg();
}

int main(void) {
    const std::string test_file = "/home/alex/Downloads/8ceattourny_d1.ch8";
    std::array<u_int8_t, 0x1000> store{};
    std::ifstream in(test_file, std::ios::in | std::ios::binary);
    if (in.is_open()) {
        in.read(reinterpret_cast<char*>(store.data() + 0x200), filesize(test_file));
    }
    for (auto &x : store) {
        std::cout << std::hex << (int)x << '\n';
    }
    return 0;
}
