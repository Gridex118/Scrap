#include <iostream>

#define MAX_STR_LEN 64

inline char char_to_upper(const char c) {
    return (c >= 'a' && c <= 'z')? c - 32 : c;
}

inline char char_to_lower(const char c) {
    return (c >= 'A' && c <= 'Z')? c + 32 : c;
}

class String {
private:
    char data_[MAX_STR_LEN];
    size_t length_ = 0;
public:
    String(): data_() {  };
    String(const char *c_str);
    String& operator= (const String &string);
    String(const String &string);
    [[ nodiscard ]] size_t length(void) const { return length_; }
    String to_upper(void) const;
    String to_lower(void) const;
    String& operator+= (const String &string);
    String operator+ (const String &string) const;
    bool operator== (const String &string) const;
    bool operator< (const String &string) const { return length_ < string.length_; }
    bool operator<= (const String &string) const { return (*this < string) || (*this == string); }
    friend std::ostream& operator<< (std::ostream &os, const String &string);
};

String::String(const char *c_str) {
    char c;
    while ((c = c_str[length_]) != '\0') {
        data_[length_++] = c;
    }
    data_[length_] = '\0';
}

String& String::operator= (const String &string) {
    length_ = string.length_;
    for (size_t i = 0; i <= length_; i++) {
        data_[i] = string.data_[i];
        // Also copy the '\0'
    }
    return *this;
}

String::String(const String &string) {
    *this = string;
}

String String::to_upper(void) const {
    String upper_string(*this);
    for (size_t i = 0; i < upper_string.length_; i++) {
        upper_string.data_[i] = char_to_upper(upper_string.data_[i]);
    }
    return upper_string;
}

String String::to_lower(void) const {
    String lower_string(*this);
    for (size_t i = 0; i < lower_string.length_; i++) {
        lower_string.data_[i] = char_to_lower(lower_string.data_[i]);
    }
    return lower_string;
}

String& String::operator+= (const String &string) {
    size_t new_length = length_ + string.length_;
    for (size_t i = length_; i < new_length; i++) {
        data_[i] = string.data_[i - length_];
    }
    length_ = new_length;
    data_[length_] = '\0';
    return *this;
}

String String::operator+ (const String &string) const {
    String concat_str(*this);
    concat_str += string;
    return concat_str;
}

bool String::operator== (const String &string) const {
    if (length_ != string.length_) return false;
    for (size_t i = 0; i < length_; i++) {
        if (data_[i] != string.data_[i]) return false;
    }
    return true;
}

std::ostream& operator<< (std::ostream &os, const String &string) {
    os << string.data_;
    return os;
}

int main(void) {
    String s("H311o th3r3");
    std::cout << s << '\n';
    String s2(s.to_lower());
    std::cout << s2 << '\n';
    String s3 = s.to_upper();
    std::cout << s3 << '\n';
    String s4 = "Whatever";
    std::cout << "s3 is " << ((s3 <= s3 + s4)? "smaller or equal to" : "larger than") << " s3 + s4\n";
    return 0;
}
