#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
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
    def isSame(self, s: TreeNode, t: TreeNode):
        if s is None and t is None:
            return True
        elif ((s is None) and (t is not None)) or ((s is not None) and (t is None)):
            return False
        result = (s.val == t.val) and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        return result
        


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        result = self.isSame(t, s) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return result

# @lc code=end

tt = TreeNode(0)

ss = TreeNode(1)

s = Solution()
print(s.isSubtree(ss, tt))

