class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1,head)
        first=second=dummy
        diff=0
        while first:
            first=first.next
            if diff<=n:
                diff+=1
            else:
                second=second.next
        second.next=second.next.next
        return dummy.next