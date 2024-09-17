#include <stdio.h>
#include <stdlib.h>

// #define MAX_QUEUE_SIZE 4

typedef struct node {
    int data;
    struct node *next;
} Node;

typedef struct {
    Node *front;
    Node *rear;
#ifdef MAX_QUEUE_SIZE
    int counter;
#endif
} Queue;

static inline int queue_is_empty(const Queue *const queue) {
    return queue->front == NULL && queue->rear == NULL;
}

Node *new_node(const int data) {
    Node *new = malloc(sizeof(Node));
    if (new != NULL) {
        new->data = data;
        new->next = NULL;
    }
    return new;
}

int insert_into_queue(Queue *const queue, const int data) {
    Node *new = new_node(data);
#ifdef MAX_QUEUE_SIZE
    if (new == NULL || queue->counter >= MAX_QUEUE_SIZE)
#else
    if (new == NULL)
#endif /* ifdef MAX_QUEUE_SIZE */
    {
        fprintf(stderr, "Overflow! could not allocate memory for new node\n");
        return -1;
    }
#ifdef MAX_QUEUE_SIZE
    ++queue->counter;
#endif /* ifdef MAX_QUEUE_SIZE */
    if (queue_is_empty(queue)) {
        queue->front = new;
        queue->rear = new;
    } else {
        queue->rear->next = new;
        queue->rear = new;
    }
    return 0;
}

int delete_from_queue(Queue *queue) {
    if (queue_is_empty(queue)) {
        fprintf(stderr, "Underflow! can not delete any more elements\n");
        return -1;
    } else {
        Node *tmp = queue->front;
        queue->front = queue->front->next;
        printf("Removing %d\n", tmp->data);
#ifdef MAX_QUEUE_SIZE
        --queue->counter;
#endif /* ifdef MAX_QUEUE_SIZE */
        free(tmp);
        if (queue->front == NULL)
            queue->rear = NULL;
    }
    return 0;
}

void display_queue_pretty(const Queue *const queue) {
    Node *iter = queue->front;
    putchar('\n');
    if (!queue_is_empty(queue)) {
        while (iter != NULL) {
            printf("%d", iter->data);
            iter = iter->next;
            if (iter != NULL) {
                printf(" -> ");
            }
        }
    } else {
        puts("Queue is empty");
    }
    putchar('\n');
}

void display_options(void) {
    puts("\n1. Insert element\n2. Remove element\n3. Print queue\n4. Exit\n");
}

int get_choice(void) {
    int choice;
    printf("Enter your choice: ");
    scanf("%d", &choice);
    return choice;
}

int insert_into_queue_input_wrapper(Queue *const queue) {
    int data;
    printf("Enter number to insert: ");
    scanf("%d", &data);
    return insert_into_queue(queue, data);
}

int main(void) {
#ifdef MAX_QUEUE_SIZE
    fprintf(stderr, "Using a fixed size for the queue");
    Queue queue = { .front = NULL, .rear = NULL, .counter = 0 };
#else
    Queue queue = {.front = NULL, .rear = NULL};
#endif /* ifdef MAX_QUEUE_SIZE */
    int running = 1;
    while (running) {
        display_options();
        switch (get_choice()) {
            case 1:
                insert_into_queue_input_wrapper(&queue);
                break;
            case 2:
                delete_from_queue(&queue);
                break;
            case 3:
                display_queue_pretty(&queue);
                break;
            case 4:
                running = 0;
                break;
            default:
                puts("Invalid choice");
        }
    }
    return 0;
}
