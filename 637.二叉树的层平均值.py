#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def dfs(self, root, level):
        if root is None:
            return
        if level in self.result:
            self.result[level][0] += root.val
            self.result[level][1] += 1
        else:
            self.result[level] = [root.val, 1]
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)



    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.result = {}
        self.dfs(root, 0)
        return [self.result[key][0] / self.result[key][1] for key in sorted(self.result)]
        
# @lc code=end

