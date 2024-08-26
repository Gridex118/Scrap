#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} Node;

Node* new_node(const int data) {
    Node *node = malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

int append_node(Node *const first, const int data) {
    Node *iter = first;
    while (iter->next != NULL) {
        iter = iter->next;
    }
    iter->next = new_node(data);
    return 0;
}

int prepend_node(Node **first, const int data) {
    Node *new = new_node(data);
    new->next = *first;
    *first = new;
    return 0;
}

int insert_node_after(Node *const first, const int data, const int after) {
    Node *iter = first;
    while (iter->data != after) {
        iter = iter->next;
        if (iter == NULL) {
            fprintf(stderr, "Could not find element\n");
            return -1;
        }
    }
    Node *tmp = iter->next;
    iter->next = new_node(data);
    iter->next->next = tmp;
    return 0;
}

int insert_node_before(Node *const first, const int data, const int before) {
    Node *iter = first;
    while (iter->next->data != before) {
        if (iter->next->next == NULL) {
            fprintf(stderr, "Could not find element\n");
            return -1;
        }
        iter = iter->next;
    }
    Node *tmp = iter->next;
    iter->next = new_node(data);
    iter->next->next = tmp;
    return 0;
}

void print_list(const Node *const first) {
    const Node *iter = first;
    while (iter != NULL) {
        printf("%d ", iter->data);
        iter = iter->next;
    }
    putchar('\n');
}

int main(void) {
    Node *first = new_node(15);
    append_node(first, 16);
    append_node(first, 17);
    append_node(first, 18);
    append_node(first, 19);
    append_node(first, 22);
    prepend_node(&first, 14);
    insert_node_after(first, 20, 19);
    insert_node_before(first, 21, 22);
    print_list(first);
    return 0;
}
