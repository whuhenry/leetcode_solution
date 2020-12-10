#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

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
    def dfs(self, root: TreeNode, result):
        if root.left is None and root.right is None:
            result.append(root.val)
        else:
            if root.left:
                self.dfs(root.left, result)
            if root.right:
                self.dfs(root.right, result)
        pass


    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        result1, result2 = [], []
        self.dfs(root1, result1)
        self.dfs(root2, result2)
        return result1 == result2

# @lc code=end

