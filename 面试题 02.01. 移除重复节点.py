# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        exist = set()
        pre = ListNode(-1)
        tmp = pre
        while head is not None:
            if head.val not in exist:
                exist.add(head.val)
                pre.next = head
                pre = pre.next
            head = head.next
        pre.next = None
        return tmp.next