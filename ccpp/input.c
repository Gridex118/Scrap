#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

char* input() {
    size_t cap = 8;
    char *ptr = (char*)malloc(sizeof(char) * cap);
    size_t i = 0;
    while (true) {    // remove leading whitespace
        int c = fgetc(stdin);
        if (c != ' ' && c != '\n') {
            ungetc(c, stdin);
            break;
        }
    }
    while (true) {
        int c = fgetc(stdin);
        if (c == '\n') break;
        ptr[i] = (char)c;
        if (i + 2 >= cap) {    // reallocate memory if cap is exceeded
                               // + 1 to account for the trailing \0
            cap *= 2;
            ptr = realloc(ptr, sizeof(char) * cap);
        }
        i++;
    }
    ptr[i] = '\0';
    return ptr;
}

int main() {
    printf("Type something: ");
    char *str = input();
    printf("%s\n", str);
    return 0;
}
