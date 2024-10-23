#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *c_left;
    struct node *c_right;
} Node;

enum TRAVERSALS { PREORDER, INORDER, POSTORDER };

Node* new_node(const int data) {
    Node *new = malloc(sizeof(Node));
    if (new) {
        new->data = data;
        new->c_left = NULL;
        new->c_right = NULL;
    }
    return new;
}

void traverse_preorder(Node *center) {
    if (!center) return;
    printf("%d ", center->data);
    traverse_preorder(center->c_left);
    traverse_preorder(center->c_right);
}

void traverse_inorder(Node *center) {
    if (!center) return;
    traverse_inorder(center->c_left);
    printf("%d ", center->data);
    traverse_inorder(center->c_right);
}

void traverse_postorder(Node *center) {
    if (!center) return;
    traverse_postorder(center->c_left);
    traverse_postorder(center->c_right);
    printf("%d ", center->data);
}

void traversal_wrapper(Node *center, enum TRAVERSALS traversal) {
    switch (traversal) {
        case PREORDER:
            printf("Preorder traversal: ");
            traverse_preorder(center);
            break;
        case INORDER:
            printf("Inorder traversal: ");
            traverse_inorder(center);
            break;
        case POSTORDER:
            printf("Postorder traversal: ");
            traverse_postorder(center);
            break;
    }
    putchar('\n');
}

int main(void) {
    Node *root = new_node(10);
    root->c_left = new_node(5);
    root->c_right = new_node(19);
    root->c_right->c_left = new_node(13);
    root->c_right->c_right = new_node(23);
    traversal_wrapper(root, PREORDER);
    traversal_wrapper(root, INORDER);
    traversal_wrapper(root, POSTORDER);
    return 0;
}
