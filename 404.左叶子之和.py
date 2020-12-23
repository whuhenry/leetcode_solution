#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def dfs(self, root: TreeNode):
        if root is None:
            return 0
        else:
            if root.left is not None and (root.left.left is None and root.left.right is None):
                self.sum += root.left.val
                self.sumOfLeftLeaves(root.right)
            else:
                self.sumOfLeftLeaves(root.left)
                self.sumOfLeftLeaves(root.right)
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.sum
        


# @lc code=end

