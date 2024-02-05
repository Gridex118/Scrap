#include <stdio.h>
#define BUF_SIZE 32

int main(void) {
    int a,b;
    printf("You know the drill: ");
    char buf[BUF_SIZE];
    if (fgets(buf, BUF_SIZE, stdin) != NULL) {
        int read = sscanf(buf, "%d %d", &a, &b);
        if (read == 2) {
            int sum = a + b;
            printf("%d + %d = %d\n",a, b, sum);
            return 0;

        }
    }
    puts("Illegal Input");
    return -1;
}
