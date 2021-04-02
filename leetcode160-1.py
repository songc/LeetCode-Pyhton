class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ta = headA
        tb = headB
        if not headA or not headB:
            return None
        while ta != tb:
            if ta:
                ta = ta.next
            else:
                ta = headB
            if tb:
                tb = tb.next
            else:
                tb = headA
        return ta