#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} Node;

Node* new_node(const int data) {
    Node *new = malloc(sizeof(Node));
    if (new != NULL) {
        new->data = data;
        new->next = NULL;
    }
    return new;
}

int push(const int data, Node **top) {
    Node *new = new_node(data);
    if (new == NULL) {
        fprintf(stderr, "Overflow; could not allocate more memory\n");
        return -1;
    }
    new->next = *top;
    *top = new;
    return 0;
}

int pop(Node **top, int *data_dump) {
    if (*top == NULL) {
        fprintf(stderr, "Underflow; can not remove more elements\n");
        return -1;
    }
    if (data_dump != NULL) {
        *data_dump = (*top)->data;
    }
    *top = (*top)->next;
    return 0;
}

void peek(const Node *top) {
    if (top == NULL) {
        puts("The stack is empty");
        return;
    }
    printf("Element on top is %d\n", top->data);
}

void display_choices() {
    puts("\n1. Push\n2. Pop\n3. Peek\n4. Exit");
}

int main(void) {
    Node *stack = NULL;
    int running = 1;
    while (running) {
        int choice;
        display_choices();
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: {
                int data;
                printf("Enter data to push: ");
                scanf("%d", &data);
                if (push(data, &stack) != 0) {
                    fprintf(stderr, "Exiting\n");
                    running = 0;
                }
                break;
            }
            case 2: {
                int data_dump;
                if (pop(&stack, &data_dump) == 0)
                    printf("Popped out %d\n", data_dump);
                break;
            }
            case 3:
                peek(stack);
                break;
            case 4:
                running = 0;
                break;
            default:
                fprintf(stderr, "Invalid choice\n");
        }
    }
    return 0;
}
