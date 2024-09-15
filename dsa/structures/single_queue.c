#include <stdio.h>
#include <stdlib.h>

#define QUEUE_LENGTH 10

typedef struct {
    int *data;
    int front;
    int back;
} Queue;

int add_element(Queue *queue, const int element) {
    if (queue->front == -1 && queue->back == -1) {
        queue->front = 0;
        queue->back = 0;
    }
    queue->data[queue->back++] = element;
    return 0;
}

int delete_element(Queue *queue) {
    if (queue->front >= queue->back) {
        fprintf(stderr, "Queue is empty\n");
        return -1;
    }
    int element = queue->data[queue->front++];
    printf("Removed %d\n", element);
    return 0;
}

int main(void) {
    Queue queue = {
        .data = malloc(QUEUE_LENGTH * sizeof(int)),
        .front = -1,
        .back = -1
    };
    add_element(&queue, 12);
    add_element(&queue, 16);
    add_element(&queue, 17);
    delete_element(&queue);
    delete_element(&queue);
    delete_element(&queue);
    delete_element(&queue);
    return 0;
}
