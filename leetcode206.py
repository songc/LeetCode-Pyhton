# 206. 反转链表
# 反转一个单链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        tmp2 = head.next
        if tmp2:
            tmp=self.reverseList(tmp2)
            tmp2.next=head
            head.next = None
            return tmp
        else:
            return head

def createListNode(lists:list):
    dummy = ListNode(0,None)
    tmp = dummy
    for i in lists:
        tmp.next=ListNode(i)
        tmp=tmp.next
    return dummy.next

sol = Solution()
nums = [1,2,3,4,5]
sol.reverseList(createListNode(nums))