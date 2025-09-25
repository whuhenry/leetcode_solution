#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = l1
        while True:
            if l2 is not None:
                l1.val = l1.val + l2.val
            if l1.val > 9:
                if l1.next is None:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1
                l1.val -= 10

            if l2 is None:
                if l1.next is None:
                    break
                else:
                    l1 = l1.next
                    continue

            if l1.next is None and l2.next is None:
                break
            elif l1.next is None and l2.next is not None:
                l1.next = l2.next
                break
            else:
                l1 = l1.next
                l2 = l2.next
        return start
        
# @lc code=end

