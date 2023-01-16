#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#

from collections import defaultdict
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
    def dfs(self, node, level):
        if node is None:
            return
        self.level_sum[level] += node.val
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)
        pass

    def maxLevelSum(self, root: TreeNode) -> int:
        self.level_sum = defaultdict(int)
        self.dfs(root, 1)
        result = self.level_sum.items()
        result.sort(key = lambda x: (x[1], -x[0]), reversed=True)
        return result[0][0]
# @lc code=end

