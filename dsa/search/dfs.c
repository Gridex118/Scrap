#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTEX_COUNT 5
#define MAX_EDGES_COUNT MAX_VERTEX_COUNT

typedef struct node {
    int dest;
    struct node* next;
} Node;

typedef struct {
    Node* head;
} AdjList;

Node* create_node(int dest) {
    Node *newNode = malloc(sizeof(Node));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}

void dfs_traversal(AdjList adj[], int visited[], int s) {
    visited[s] = 1;
    printf("%d ", s);
    Node* current = adj[s].head;
    while (current != NULL) {
        int dest = current->dest;
        if (!visited[dest]) {
            dfs_traversal(adj, visited, dest);
        }
        current = current->next;
    }
}

void dfs(AdjList adj[], int s) {
    int visited[5] = {0}; 
    dfs_traversal(adj, visited, s);
}

void add_edge(AdjList adj[], int s, int t) {
    Node* newNode = create_node(t);
    newNode->next = adj[s].head;
    adj[s].head = newNode;
    newNode = create_node(s);
    newNode->next = adj[t].head;
    adj[t].head = newNode;
}

int main() {
    AdjList adj_list[MAX_VERTEX_COUNT];
    for (int i = 0; i < MAX_VERTEX_COUNT; i++) {
        adj_list[i].head = NULL;
    }
    int edges[][2] = {
        {1, 2}, {1, 0}, {2, 0}, {2, 3}, {2, 4}
    };
    for (int i = 0; i < MAX_EDGES_COUNT; i++) {
        add_edge(adj_list, edges[i][0], edges[i][1]);
    }
    int source = 1; 
    printf("DFS from source: %d\n", source);
    dfs(adj_list, source);
    return 0;
}
