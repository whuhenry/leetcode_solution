#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        if head.val == 1000000:
            return True
        else:
            head.val = 1000000
            if head.next is None:
                return False
            else:
                return self.hasCycle(head.next)
# @lc code=end

