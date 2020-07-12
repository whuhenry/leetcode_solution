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
    TreeNode* dfs(vector<int> nums, int start, int end){
        if (start > end) {
            return nullptr;
        }
        if (start == end) {
            TreeNode* node = new TreeNode(nums[start]);
            return node;
        }
        int center = (start + end) / 2;
        TreeNode* node = new TreeNode(nums[center]);
        node->left = dfs(nums, start, center -1);
        node->right = dfs(nums, center + 1, end);
        return node;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode *head = dfs(nums, 0, nums.size() - 1);
        return head;
    }
};