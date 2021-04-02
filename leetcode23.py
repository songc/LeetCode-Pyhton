# 23. 合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。

# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import bisect
import collections
class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        dummy = ListNode()
        tmp = dummy
        deque = collections.deque(maxlen=len(lists))
        for head in lists:
            if head:
                self.insort_left(deque,head)
        while deque:
            node=deque.popleft()
            tmp.next=node
            tmp = tmp.next
            if node.next:
                self.insort_left(deque,node.next)
            if len(deque)==1:
                tmp.next=deque.pop()
                break
        return dummy.next

    def insort_left(self, deque:collections.deque, node:ListNode):
        lo = 0
        hi = len(deque)
        while(lo<hi):
            mid = (lo+hi)//2
            if deque[mid].val==node.val:
                hi=mid
            elif deque[mid].val<node.val:
                lo=mid+1
            elif deque[mid].val>node.val:
                hi=mid
        deque.insert(lo, node)

        
        
        