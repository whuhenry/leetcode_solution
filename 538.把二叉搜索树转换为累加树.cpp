/*
 * @lc app=leetcode.cn id=538 lang=cpp
 *
 * [538] 把二叉搜索树转换为累加树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    void search(TreeNode *node) {
        if (nullptr !=  node->right) {
            search(node->right);
        }
        sum += node->val;
        node->val = sum;
        if (nullptr != node->left) {
            search(node->left);
        }
    }

    TreeNode* convertBST(TreeNode* root) {
        if (nullptr == root) {
            return root;
        }
        search(root);
        return root;
    }
};
// @lc code=end

