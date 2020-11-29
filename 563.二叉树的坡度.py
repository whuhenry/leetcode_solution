#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute(self, root: TreeNode):
        """
            return sum, diff
        """
        if root is None:
            return 0
        left = self.compute(root.left)
        right = self.compute(root.right)
        self.result += abs(left - right)
        return left + right + root.val
        

    def findTilt(self, root: TreeNode) -> int:
        self.result = 0
        self.compute(root)
        return self.result
        
# @lc code=end

