# 61. 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        diff = k % n
        if diff == 0:
            return head
        fast = slow = head
        while fast.next:
            if diff > 0:
                fast = fast.next
                diff -= 1
                continue
            fast = fast.next
            slow = slow.next
        dummy = slow.next
        slow.next = None
        fast.next = head
        return dummy
