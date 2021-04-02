class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1,head)
        tmpHead= dummy
        tail = dummy
        count=0
        while tail.next:
            tail=tail.next
            count+=1
            if count%k == 0:
                tmp=tmpHead.next
                tmpHead.next=self.reverseHeadTail(tmpHead.next,tail)
                tmpHead=tail=tmp
        return dummy.next



    def reverseHeadTail(self,head:ListNode, tail:ListNode)-> ListNode:
        dummy=ListNode(-1,tail)
        tmp =head
        while tmp!=tail:
            tmpNext = tail.next
            tail.next=tmp
            tmp=tmp.next
            tail.next.next=tmpNext
        return dummy.next

l1 = ListNode(0)
l3=ListNode(8)
l4=ListNode(9)
l2 = ListNode(2)
l5= ListNode(7)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5 


sol = Solution()

print(sol.reverseKGroup(l1,3))


        