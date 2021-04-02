# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        l3 = ListNode()
        tmp3 = l3
        tmp1 = l1
        tmp2 = l2
        while(tmp1.val or tmp1.next or tmp2.val or tmp2.next or temp):
            tmp3.val = (tmp1.val+tmp2.val+temp)%10
            temp = (tmp1.val+tmp2.val+temp)//10
            if tmp1.next:
                tmp1=tmp1.next
            else:
                tmp1 = ListNode()
            if tmp2.next:
                tmp2=tmp2.next
            else:
                tmp2 = ListNode()
            if tmp1.val or tmp1.next or tmp2.val or tmp2.next or temp:
                tmp3.next=ListNode()
                tmp3=tmp3.next
            else:
                break 
        return l3
l1 = ListNode(0)
l1.next=ListNode(3)
l2 = ListNode(0)
l2.next=ListNode(7)
 
s= Solution()
l3 = s.addTwoNumbers(l1,l2)
print(l3)


            
            
