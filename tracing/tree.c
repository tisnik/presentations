#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct Node
{
    struct Node *left;
    struct Node *right;
    char *value;
} Node;

void insert_new_node(Node **root, char *value)
{
    int cmp;

    if (*root == NULL)
    {
        *root = (Node *)malloc(sizeof(Node));
        (*root)->value = (char*)calloc(strlen(value), sizeof(char));
        strcpy((*root)->value, value);
        (*root)->left = NULL;
        (*root)->right = NULL;
        return;
    }
    cmp = strcmp(value, (*root)->value);
    if (cmp < 0)
    {
        insert_new_node(&(*root)->left, value);
    }
    else
    {
        insert_new_node(&(*root)->right, value);
    }
}

void traverse_tree(Node *root, void (*callback_function)(char *))
{
    if (root == NULL)
    {
        return;
    }
    traverse_tree(root->left, callback_function);
    callback_function(root->value);
    traverse_tree(root->right, callback_function);
}

void callback_function(char *value)
{
    printf("%s\n", value);
}

int main(void)
{
    static Node *root = NULL;

    insert_new_node(&root, "xxx");
    insert_new_node(&root, "aaa");
    insert_new_node(&root, "bbb");
    insert_new_node(&root, "ccc");
    insert_new_node(&root, "yyy");
    insert_new_node(&root, "yyy");

    traverse_tree(root, callback_function);

    return 0;
}

