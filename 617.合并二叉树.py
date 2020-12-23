#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        else:
            if t1 is None and t2 is not None:
                t1 = t2
            elif t1 is not None and t2 is not None:
                t1.val += t2.val
                t1.left = self.mergeTrees(t1.left, t2.left)
                t1.right = self.mergeTrees(t1.right, t2.right)
                
            return t1

        
# @lc code=end

