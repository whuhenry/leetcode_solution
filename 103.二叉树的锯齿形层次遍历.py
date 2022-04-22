#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        curlayer = [root]
        dir = False
        result = []
        while curlayer:
            result.append([node.val for node in curlayer])
            next_layer = []
            curlayer = curlayer[::-1]
            for node in curlayer:
                if dir:
                    if node.left is not None:
                        next_layer.append(node.left)
                    if node.right is not None:
                        next_layer.append(node.right)
                else:
                    if node.right is not None:
                        next_layer.append(node.right)
                    if node.left is not None:
                        next_layer.append(node.left)
            curlayer = next_layer
            dir = not dir
        return result

# @lc code=end

