#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result = -1
        node_list = [root]
        while node_list:
            new_list = []
            for node in node_list:
                if node.val > root.val:
                    result = min(result, node.val) if result < 0 else node.val
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
            node_list = new_list
        return result

# @lc code=end

