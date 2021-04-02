class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            if fast == slow:
                return True
            slow = slow.next
        return False