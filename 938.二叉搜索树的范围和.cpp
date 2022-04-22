/*
 * @lc app=leetcode.cn id=938 lang=cpp
 *
 * [938] 二叉搜索树的范围和
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
    int rangeSumBST(TreeNode* root, int L, int R) {
        if (root == nullptr) { return 0;}
        int thisAdd = 0;
        if (root->val >= L && root->val <= R) {
            thisAdd = root->val;
        }
        return rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R) + thisAdd;
    }
};
// @lc code=end

