# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                fast=head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast   
        return None