#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

void input_strip_ws() {
    while (true) {
        char c = fgetc(stdin);
        if (c != ' ' && c != '\n') {
            ungetc(c, stdin);
            break;
        }
    }
}

char* input() {
    input_strip_ws();
    size_t cap = 16;
    char *input_buf = (char*)malloc(sizeof(char) * cap);
    size_t i = 0;
    while (true) {
        char c = fgetc(stdin);
        if (c == '\n') break;
        input_buf[i] = c;
        if (i + 2 >= cap) {    // reallocate memory if cap is exceeded
                               // + 1 to account for the trailing \0
            cap *= 2;
            input_buf = realloc(input_buf, sizeof(char) * cap);
        }
        i++;
    }
    input_buf[i] = '\0';
    return input_buf;
}

int main() {
    printf("Type something: ");
    char *str = input();
    if (str == NULL) return -1;
    printf("%s\n", str);
    return 0;
}
