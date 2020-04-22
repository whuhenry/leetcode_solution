/*
 * @lc app=leetcode.cn id=199 lang=cpp
 *
 * [199] 二叉树的右视图
 */
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

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
    vector<int> rightSideView(TreeNode* root) {
        vector<TreeNode*> levelList;
        vector<int> result;
        if (nullptr == root) {
            return result;
        }
        levelList.push_back(root);
        while(!levelList.empty()){
            vector<TreeNode*> nextList;
            result.push_back(levelList[0]->val);
            for (int i = 0; i < levelList.size(); ++i) {
                if (nullptr != levelList[i]->right) {
                    nextList.push_back(levelList[i]->right);
                }
                if (nullptr != levelList[i]->left) {
                    nextList.push_back(levelList[i]->left);
                }
            }
            levelList.swap(nextList);
        }
        return result;
    }
};
// @lc code=end

