#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: TreeNode) -> bool:

        def dfs(node1: TreeNode, node2: TreeNode):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is not None:
                return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            else:
                return False
        
        if root is None:
            return True
        else:
            return dfs(root.left, root.right)


        
# @lc code=end

