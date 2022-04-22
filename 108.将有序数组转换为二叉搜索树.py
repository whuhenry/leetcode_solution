#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def build_tree(start, end):
            if start > end:
                return None
            center = (start + end) // 2
            node = TreeNode(nums[center])
            node.left = build_tree(start, center - 1)
            node.right = build_tree(center + 1, end)
            return node
        
        return build_tree(0, len(nums) - 1)

# @lc code=end

