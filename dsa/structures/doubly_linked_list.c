#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *left;
    struct node *right;
} Node;

Node* new_node(const int data) {
    Node *new = malloc(sizeof(Node));
    if (new != NULL) {
        new->data = data;
        new->left = NULL;
        new->right = NULL;
    } else {
        fprintf(stderr, "Overflow, can not create more nodes\n");
    }
    return new;
}

int prepend_node(Node **first, const int data) {
    Node *new = new_node(data);
    if (new == NULL) return -1;
    new->right = *first;
    *first = new;
    return 0;
}

int append_node(Node **first, const int data) {
    Node *new = new_node(data);
    if (new == NULL) return -1;
    if (*first == NULL) {
        *first = new;
        return 0;
    }
    Node *iter = *first;
    while (iter->right != NULL) {
        iter = iter->right;
    }
    iter->right = new;
    new->left = iter;
    return 0;
}

int insert_node_after(Node **first, const int key, const int data) {
    Node *new = new_node(data);
    if (new == NULL) return -1;
    Node *iter = *first;
    while (iter->data != key) {
        iter = iter->right;
        if (iter == NULL) {
            puts("Could not find node");
            return 0;
        }
    }
    new->left = iter;
    new->right = iter->right;
    iter->right = new;
    return 0;
}

void print_list(const Node *const first) {
    const Node *tmp = first;
    while (tmp != NULL) {
        printf("%d ", tmp->data);
        tmp = tmp->right;
    }
}

int main(void) {
    Node *first = NULL;
    prepend_node(&first, 15);
    prepend_node(&first, 14);
    append_node(&first, 17);
    prepend_node(&first, 13);
    insert_node_after(&first, 15, 16);
    print_list(first);
    return 0;
}
