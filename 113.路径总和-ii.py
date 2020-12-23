#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root: TreeNode):
        if root is None:
            return
        self.path.append(root.val)
        self.path_sum += root.val
        
        if root.left is None and root.right is None:
            if self.path_sum == self.target:
                self.result.append(self.path.copy())

        self.dfs(root.left)
        self.dfs(root.right)
        self.path.pop()
        self.path_sum -= root.val
        pass
        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.path = []
        self.result = []
        self.path_sum = 0
        self.target = sum
        self.dfs(root)
        return self.result

# @lc code=end

