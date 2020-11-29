#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def midTraversal(self, root: TreeNode):
        if root is None:
            return
        self.midTraversal(root.left)
        if self.pre is not None:
            if self.result is None:
                self.result = root.val - self.pre
            else:
                self.result = min(self.result, root.val - self.pre)
        self.pre = root.val
        self.midTraversal(root.right)

    def minDiffInBST(self, root: TreeNode) -> int:
        self.pre = None
        self.result = None
        self.midTraversal(root)
        return self.result
# @lc code=end

