#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
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

import collections

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(node: TreeNode):
            if node is None:
                return
            else:
                self.num_dict[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        self.num_dict = collections.defaultdict(int)
        dfs(root)
        sta = list(self.num_dict.items())
        sta.sort(key= lambda x:(x[1]), reverse=True)
        result = []
        for i in range(len(sta)):
            if sta[i][1] == sta[0][1]:
                result.append(sta[i][0])
            else:
                break
        return result
# @lc code=end

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node1.right = node2
node2.left = node3


s = Solution()
print(s.findMode(None))
