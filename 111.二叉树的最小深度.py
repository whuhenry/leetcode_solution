#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            if root.left is None and root.right is None:
                return 1
            result = 1000000
            if root.left is not None:
                result = min(result, self.minDepth(root.left))
            if root.right is not None:
                result = min(result, self.minDepth(root.right))

            return 1 + result
# @lc code=end

