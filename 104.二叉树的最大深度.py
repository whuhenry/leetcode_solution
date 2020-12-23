#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
        self.result = 0


    def dfs(self, node, depth):
        if node is None or node.val is None:
            return
        self.result = max(self.result, depth)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)

    def maxDepth(self, root: TreeNode) -> int:
        result = 0
        self.dfs(root, 1)
        return self.result
# @lc code=end

