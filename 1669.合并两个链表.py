#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        count1 = -1
        virtual_head = ListNode(-1)
        virtual_head.next = list1
        ptr_a = ptr_b = virtual_head
        ptr1 = virtual_head
        while count1 <= b:
            if count1 == a - 1:
                ptr_a = ptr1
            if count1 == b:
                ptr_b = ptr1
            ptr1 = ptr1.next
            count1 += 1
        ptr_a.next = list2
        tail2.next = ptr_b.next
        return  virtual_head.next
# @lc code=end

