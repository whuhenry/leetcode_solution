#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        backup = head
        while head is not None:
            count += 1
            head = head.next

        idx = count // 2

        count = 0
        head = backup
        while head is not None:
            if count == idx:
                return head
            else:
                count += 1
            
            head = head.next
                
        return None
        
# @lc code=end

