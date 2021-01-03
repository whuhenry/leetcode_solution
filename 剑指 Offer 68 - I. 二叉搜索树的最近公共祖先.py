class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        self.result_level = -1
        def dfs(node, level):
            if node is None:
                return False, False
            flag_p = False
            flag_q = False
            if node == p:
                flag_p = True
            elif node == q:
                flag_q = True
            flag_pl, flag_ql = dfs(node.left, level + 1)
            flag_pr, flag_qr = dfs(node.right, level + 1)

            result_p = flag_p or flag_pl or flag_pr
            result_q = flag_q or flag_ql or flag_qr

            if result_p and result_q and level > self.result_level:
                self.result = node
                self.result_level = level

            return result_p, result_q

        dfs(root, 0)
        return self.result
        
s = Solution()

node1 = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4
print(s.lowestCommonAncestor(node1, node2, node4).val)