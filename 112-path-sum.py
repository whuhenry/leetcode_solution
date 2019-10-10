# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calcSum(self, curNode: TreeNode):
        if self.hasSum:
            return
        
        self.findSum += curNode.val
        if curNode.left == None and curNode.right == None:
            if self.findSum == self.targetSum:
                self.hasSum = True
        else:
            if curNode.left != None:
                calcSum(curNode.left)
            if curNode.right != None:
                calcSum(curNode.right)
        self.findSum -= curNode.val
        

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.hasSum = False
        self.findSum = 0
        self.targetSum = sum
        if root == None:
            return False
        self.calcSum(root)
        return self.hasSum
        
        