#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if root.children is None or len(root.children) == 0:
            return 1
        return max([self.maxDepth(child) + 1 for child in root.children])
# @lc code=end

