# 82. 删除排序链表中的重复元素 II
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0,head)
        pre = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur = cur.next
                cur=cur.next
                pre.next=cur
            else:
                pre = cur
                cur=cur.next
        return dummy.next
            