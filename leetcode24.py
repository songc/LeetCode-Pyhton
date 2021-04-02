# 24. 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=ListNode(next=head)
        count=0
        node1=dummy
        node2=dummy
        while node1:          
            if count>0 and count%2==0:
                tmp = node2.next
                tmp.next=node1.next
                node2.next=node1
                node1.next = tmp
                node1=node2=tmp
            node1=node1.next
            count+=1                         
        return dummy.next

l1 = ListNode(0)
l3=ListNode(8)
l4=ListNode(9)
l2 = ListNode(2)
l1.next=l2
l2.next=l3
# l3.next=l4


sol = Solution()

print(sol.swapPairs(l1))