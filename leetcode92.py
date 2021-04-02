92. 反转链表 II
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0,head)
        diff = right-left
        fast = slow = head
        pre  = dummy
        for i in range(diff):
            fast = fast.next
        for i in range(left-1):
            pre = slow
            slow = slow.next
            fast = fast.next
        while slow != fast:
            tmp = slow
            slow = slow.next
            tmp.next = fast.next
            fast.next = tmp
            pre.next = slow
        return dummy.next