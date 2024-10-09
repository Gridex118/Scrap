#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *left;
    struct node *right;
} Node;

enum POSITIONS { BEGINNING, END, AFTER };

static inline int list_is_empty(const Node *const first) {
    return first == NULL;
}

static inline int list_is_singleton(const Node *const first) {
    return first->right == NULL;
}

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
    if (new->right != NULL)
        (new->right)->left = new;
    *first = new;
    return 0;
}

int delete_beginning(Node **first) {
    if (list_is_empty(*first)) {
        fprintf(stderr, "Underflow, can not remove more nodes\n");
        return -1;
    }
    Node *tmp = *first;
    *first = (*first)->right;
    if (!list_is_empty(*first))
        (*first)->left = NULL;
    printf("Popping out %d\n", tmp->data);
    free(tmp);
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

int delete_end(Node **first) {
    if (list_is_empty(*first)) {
        fprintf(stderr, "Underflow, can not remove more nodes\n");
        return -1;
    }
    Node *to_delete;
    if (list_is_singleton(*first)) {
        to_delete = *first;
        *first = NULL;
    } else {
        Node *tmp = *first;
        while (tmp->right != NULL)
            tmp = tmp->right;
        (tmp->left)->right = NULL;
        to_delete = tmp;
    }
    printf("Popping out %d\n", to_delete->data);
    free(to_delete);
    return 0;
}

int insert_node_after_specific(Node **first, const int key, const int data) {
    Node *new = new_node(data);
    if (new == NULL) return -1;
    Node *iter = *first;
    while (iter->data != key) {
        iter = iter->right;
        if (iter == NULL) {
            puts("Could not find node");
            return -1;
        }
    }
    new->left = iter;
    new->right = iter->right;
    iter->right = new;
    return 0;
}

int delete_specific(Node **first, const int key) {
    if (list_is_empty(*first)) {
        fprintf(stderr, "Underflow, can not remove more nodes\n");
        return -1;
    }
    Node *tmp = *first;
    while (tmp->data != key) {
        tmp = tmp->right;
        if (tmp == NULL) {
            puts("Could not find node");
            return -1;
        }
    }
    if (tmp->left != NULL)
        (tmp->left)->right = tmp->right;
    if (tmp->right != NULL)
        (tmp->right)->left = tmp->left;
    if (tmp == *first)
        *first = tmp->right;
    printf("Popping out %d\n", tmp->data);
    free(tmp);
    return 0;
}

void print_list(const Node *const first) {
    if (list_is_empty(first)) {
        puts("Empty list");
    } else {
        for (const Node *tmp = first; tmp != NULL; tmp = tmp->right)
            printf("%d ", tmp->data);
    }
    putchar('\n');
}

int insertion_input_wrapper(Node **first, enum POSITIONS position) {
    int data;
    printf("Enter element to insert: ");
    scanf("%d", &data);
    switch (position) {
        case BEGINNING: return prepend_node(first, data);
        case END: return append_node(first, data);
        case AFTER: {
            int key;
            printf("Enter key: ");
            scanf("%d", &key);
            return insert_node_after_specific(first, key, data);
        }
        default: return -1;
    }
}

int deletion_input_wrapper(Node **first, enum POSITIONS position) {
    switch (position) {
        case BEGINNING: return delete_beginning(first);
        case END: return delete_end(first);
        case AFTER: {
            int key;
            printf("Enter key: ");
            scanf("%d", &key);
            return delete_specific(first, key);
        }
        default: return -1;
    }
}

void print_options(void) {
    puts("1. Insert at beginning\n2. Insert at end\n3. Insert after an element");
    puts("4. Delete at beginning\n5. Delete at end\n6. Delete specific element");
    puts("7. Print list\n8. Exit");
}

int get_choice(void) {
    print_options();
    int choice;
    printf("Enter your choice: ");
    scanf("%d", &choice);
    return choice;
}

int main(void) {
    Node *first = NULL;
    int running = 1;
    while (running) {
        switch (get_choice()) {
            case 1: insertion_input_wrapper(&first, BEGINNING);
                break;
            case 2: insertion_input_wrapper(&first, END);
                break;
            case 3: insertion_input_wrapper(&first, AFTER);
                break;
            case 4: deletion_input_wrapper(&first, BEGINNING);
                break;
            case 5: deletion_input_wrapper(&first, END);
                break;
            case 6: deletion_input_wrapper(&first, AFTER);
                break;
            case 7: print_list(first);
                break;
            case 8: running = 0;
                break;
        }
    }
    return 0;
}
