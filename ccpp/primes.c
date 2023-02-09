#include "stdio.h"

#define BOTTOM 2
#define TOP 2000

int main() {
    for (int i=BOTTOM; i<=TOP; ++i) {
        int j=BOTTOM;
        for (j; j<i; ++j) {
            if ((i%j == 0) && i != 2) break;
        }
        if (j==i) printf("%d\n",i);
    }
    return 0;
}

