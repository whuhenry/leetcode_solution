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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (nullptr == p && nullptr == q) {
            return true;
        } else if ((nullptr != p && nullptr == q) || (nullptr == p && nullptr != q)) {
            return false;
        }
        
        bool sameroot = (p->val == q->val);
        if (!sameroot) {
            return false;
        }
        //left
        bool sameleft = false, sameright = false;
        if (nullptr == p->left && nullptr == q->left) {
            sameleft = true;
        } else if ((nullptr == p->left && nullptr != q->left) 
                   || (nullptr != p->left && nullptr == q->left)) {
            return false;
        } else if (!isSameTree(p->left, q->left)) {
                return false;
        } else {
            sameleft = true;
        }
        
        //right
        if (nullptr == p->right && nullptr == q->right) {
            sameright = true;
        } else if ((nullptr == p->right && nullptr != q->right) 
                   || (nullptr != p->right && nullptr == q->right)) {
            return false;
        } else if (!isSameTree(p->right, q->right)) {
                return false;
        } else {
            sameright = true;
        }
        
        return true;
    }
};