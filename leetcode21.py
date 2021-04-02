# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=tmp = ListNode()
        while l1 or l2:
            if l1==None:
                tmp.next=l2
                break
            if l2==None:
                tmp.next=l1
                break
            if l1.val<=l2.val:
                tmp.next=l1
                l1=l1.next
                tmp=tmp.next
            else:
                tmp.next=l2
                l2=l2.next
                tmp=tmp.next
        return dummy.next