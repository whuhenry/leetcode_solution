#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

from typing import List

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
        self.result = []
        self.path = []

    def dfs(self, node):
        if node is None:
            return
        self.path.append(str(node.val))

        if node.left is None and node.right is None:
            self.result.append('->'.join(self.path))
        else:
            self.dfs(node.left)
            self.dfs(node.right)

        self.path.pop()
        return


    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.dfs(root)
        return self.result
# @lc code=end

