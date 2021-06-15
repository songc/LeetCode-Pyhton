# 203. 移除链表元素
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from ListNodeUtil import createListNode
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0,head)
        pre = dummy
        while pre.next:
            if pre.next.val==val:
                pre.next=pre.next.next
                continue
            pre=pre.next
        return dummy.next
    
sol = Solution()
head = [1,2,6,3,4,5,6]
val = 6
head = createListNode(head)
print(sol.removeElements(head,val))