#include <stdio.h>

#define TABLE_CAP 100
#define MODULUS   97

typedef struct {
    int data[TABLE_CAP];
    int used_keys[TABLE_CAP];
    int size;
} HTable;

void init_h_table(HTable *h_table_p) {
    for (int i = 0; i < TABLE_CAP; ++i) {
        h_table_p->data[i] = 0;
        h_table_p->used_keys[i] = 0;
    }
    h_table_p->size = 0;
}

static inline int key_is_used(const HTable *h_table_p, unsigned key) {
    return h_table_p->used_keys[key];
}

unsigned hash_function_division(const int x) {
    return x % MODULUS;
}

int insert_into_table(HTable *h_table_p, const int x) {
    if (h_table_p->size++ < TABLE_CAP) {
        unsigned key = hash_function_division(x);
        if (!key_is_used(h_table_p, key)) {
            h_table_p->data[key] = x;
            h_table_p->used_keys[key] = 1;
            return 0;
        } else {
            fprintf(stderr, "Key collision occured\n");
            return -1;
        }
    } else {
        fprintf(stderr, "Capacity exceeded\n");
        return -1;
    }
}

void print_h_table(const HTable *const h_table_p) {
    for (int i = 0; i < TABLE_CAP; ++i) {
        if (key_is_used(h_table_p, i)) {
            printf("%04d: %-hd\n", h_table_p->data[i], i);
        }
    }
}

int main(void) {
    HTable h_table;
    init_h_table(&h_table);
    int records[] = {
        180, 288, 591, 283, 332, 210, 729, 100,
        182, 5891, 1081, 1882, 566
    };
    int rec_len = (sizeof records / sizeof records[0]);
    for (int i = 0; i < rec_len; ++i) {
        insert_into_table(&h_table, records[i]);
    }
    puts("Resultant hash table");
    print_h_table(&h_table);
    return 0;
}
