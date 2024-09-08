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

int delete_node_start(Node **head, int *item_dump) {
    if (*head == NULL) {
        fprintf(stderr, "Empty, can not delete anymore\n");
        return -1;
    }
    Node *tmp = *head;
    *head = (*head)->next;
    *item_dump = tmp->data;
    free(tmp);
    return 0;
}

int delete_node_end(Node **head, int *item_dump) {
    if (*head == NULL) {
        fprintf(stderr, "Empty, can not delete anymore\n");
        return -1;
    }
    Node *iter = *head;
    if ((*head)->next == NULL) {
        free(iter);
        *head = NULL;
        return 0;
    }
    Node *iter_prev = iter;
    while (iter->next != NULL) {
        iter_prev = iter;
        iter = iter->next;
    }
    iter_prev->next = NULL;
    *item_dump = iter->data;
    free(iter);
    return 0;
}

int delete_node_at(Node **head, const int key, int *item_dump) {
    if (*head == NULL) {
        fprintf(stderr, "Empty, can not delete anymore\n");
        return -1;
    }
    Node *iter = *head;
    if ((*head)->next == NULL) {
        free(iter);
        *head = NULL;
        return 0;
    }
    Node *iter_prev = iter;
    while (iter->data != key) {
        iter_prev = iter;
        iter = iter->next;
        if (iter == NULL) {
            fprintf(stderr, "Could not find element\n");
            return -1;
        }
    }
    iter_prev->next = iter->next;
    *item_dump = iter->data;
    free(iter);
    return 0;
}

void reverse_list(Node **head) {
    Node *current = *head;
    Node *previous = NULL;
    Node *next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }
    *head = previous;
}

void print_list(const Node *const head) {
    const Node *iter = head;
    while (iter != NULL) {
        printf("%d ", iter->data);
        iter = iter->next;
    }
    putchar('\n');
}

void display_choices() {
    putchar('\n');
    puts("1. Prepend node\n2. Append node\n3. Insert node after");
    puts("4. Delete node at beginning\n5. Delete node at end\n6. Delete node at");
    puts("7. Reverse list");
    puts("8. Exit");
}

int continuation_prompt() {
    char continuation_choice;
    printf("Continue operations(y/n)? ");
    scanf(" %c", &continuation_choice);
    return (continuation_choice == 'y');
}

int main(void) {
    int first_elem;
    printf("Initialize list with element(integer): ");
    scanf("%d", &first_elem);
    Node *head = new_node(first_elem);
    int choice;
    int running = 1;
    while (running) {
        puts("Current list:");
        print_list(head);
        display_choices();
        printf("Enter your choice: ");
        scanf("%d", &choice);
        int data_input;
        int data_dump;
        if (choice >= 1 && choice <= 3) {
            printf("Enter data to input: ");
            scanf("%d", &data_input);
        }
        switch (choice) {
            case 1:
                prepend_node(&head, data_input);
                break;
            case 2:
                append_node(head, data_input);
                break;
            case 3:
                {
                    int after;
                    printf("Insert after: ");
                    scanf("%d", &after);
                    insert_node_after(head, data_input, after);
                    break;
                }
            case 4:
                delete_node_start(&head, &data_dump);
                break;
            case 5:
                delete_node_end(&head, &data_dump);
                break;
            case 6:
                {
                    int at;
                    printf("Delete at: ");
                    scanf("%d", &at);
                    delete_node_at(&head, at, &data_dump);
                    break;
                }
            case 7:
                reverse_list(&head);
                break;
            case 8:
                running = 0;
                break;
            default:
                puts("Invalid choice");
        }
        if (running) {
            running = continuation_prompt();
        }
    }
    puts("\nFinal list");
    print_list(head);
    return 0;
}
