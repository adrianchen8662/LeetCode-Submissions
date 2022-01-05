/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isBalanced(struct TreeNode* root);
int max(int a, int b);
int height(struct TreeNode* node);

bool isBalanced(struct TreeNode* root){
    int lh;
    int rh;

    if (root == NULL)
        return 1;

    lh = height(root->left);
    rh = height(root->right);
 
    if (abs(lh - rh) <= 1 && isBalanced(root->left) && isBalanced(root->right))
        return 1;

    return 0;
}

int max(int a, int b)
{
    return (a >= b) ? a : b;
}

int height(struct TreeNode* node)
{
    if (node == NULL)
        return 0;

    return 1 + max(height(node->left), height(node->right));
}