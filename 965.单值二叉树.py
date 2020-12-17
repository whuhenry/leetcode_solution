#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.val = None

    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if self.val is None:
            self.val = root.val
        return (self.val == root.val) & self.isUnivalTree(root.left) & self.isUnivalTree(root.right)
        
# @lc code=end

