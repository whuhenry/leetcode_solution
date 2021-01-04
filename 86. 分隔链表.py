# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        little_head, big_head = ListNode(-1), ListNode(-1)
        little_tail, big_tail = little_head, big_head
        while head is not None:
            if head.val < x:
                little_tail.next = head
                little_tail = little_tail.next
            else:
                big_tail.next = head
                big_tail = big_tail.next
            head = head.next
        little_tail.next = big_head
        big_tail.next = None
        return little_head.next