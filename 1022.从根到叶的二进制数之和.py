#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            self.bits = (self.bits << 1) + node.val
            if node.left is None and node.right is None:
                self.result += self.bits
            else:
                if node.left is not None:
                    dfs(node.left)
                if node.right is not None:
                    dfs(node.right)
            
            self.bits = self.bits >> 1

        self.result = 0
        self.bits = 0
        dfs(root)
        return self.result


# @lc code=end

s = Solution()

node1 =TreeNode(1)
node2 =TreeNode(0)
node3 =TreeNode(1)
node4 =TreeNode(0)
node5 =TreeNode(1)
node6 =TreeNode(0)
node7 =TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print(s.sumRootToLeaf(node1))