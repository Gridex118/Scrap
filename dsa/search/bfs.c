#include <stdio.h>

#define MAX_LIST_NODES 100

typedef struct {
    int data[MAX_LIST_NODES];
    int front;
    int rear;
} Queue;

void init_queue(Queue *queue_p) {
    queue_p->front = 0;
    queue_p->rear = 0;
}

void bfs(int adj_list[MAX_LIST_NODES][MAX_LIST_NODES], int vertices, int source) {
    Queue queue;
    init_queue(&queue);
    int visited[MAX_LIST_NODES] = {};
    visited[source] = 1;
    queue.data[queue.rear++] = source;
    while (queue.front < queue.rear) {
        int current = queue.data[queue.front++];
        printf("%d ", current);
        for (int i = 0; i < vertices; i++) {
            if (adj_list[current][i] == 1 && !visited[i]) {
                visited[i] = 1;
                queue.data[queue.rear++] = i;
            }
        }
    }
}

void add_edge(int adj_list[MAX_LIST_NODES][MAX_LIST_NODES], int u, int v) {
    adj_list[u][v] = 1;
    adj_list[v][u] = 1;
}

int main(void) {
    int V = 5;
    int adj_list[MAX_LIST_NODES][MAX_LIST_NODES] = { 0 };
    add_edge(adj_list, 0, 1);
    add_edge(adj_list, 0, 2);
    add_edge(adj_list, 1, 3);
    add_edge(adj_list, 1, 4);
    add_edge(adj_list, 2, 4);
    puts("BFS starting from 0:");
    bfs(adj_list, V, 0);
    return 0;
}
