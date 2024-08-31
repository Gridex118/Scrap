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

int append_node(Node *const head, const int data) {
    Node *iter = head;
    while (iter->next != NULL) {
        iter = iter->next;
    }
    iter->next = new_node(data);
    return 0;
}

int prepend_node(Node **head, const int data) {
    Node *new = new_node(data);
    new->next = *head;
    *head = new;
    return 0;
}

int insert_node_after(Node *const head, const int data, const int after) {
    Node *iter = head;
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

int insert_node_before(Node *const head, const int data, const int before) {
    Node *iter = head;
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

int delete_node_back(Node **head) {
    if (*head == NULL) {
        fprintf(stderr, "Empty, can not delete anymore\n");
        return -1;
    }
    Node *tmp = *head;
    *head = (*head)->next;
    free(tmp);
    return 0;
}

int delete_node_front(Node *head) {
    if (head == NULL) {
        fprintf(stderr, "Empty, can not delete anymore\n");
        return -1;
    }
    Node *iter = head;
    Node *iter_prev = iter;
    while (iter->next != NULL) {
        iter_prev = iter;
        iter = iter->next;
    }
    iter_prev->next = NULL;
    free(iter);
    return 0;
}

void print_list(const Node *const head) {
    const Node *iter = head;
    while (iter != NULL) {
        printf("%d ", iter->data);
        iter = iter->next;
    }
    putchar('\n');
}

int main(void) {
    Node *head = new_node(15);
    append_node(head, 16);
    delete_node_front(head);
    print_list(head);
    return 0;
}
