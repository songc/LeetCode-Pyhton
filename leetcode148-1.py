
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(node1, node2):
            dummy = ListNode(0)
            tmp = dummy
            tmp1, tmp2 = node1, node2
            while tmp1 and tmp2:
                if tmp1.val < tmp2.val:
                    tmp.next = tmp1
                    tmp = tmp.next
                    tmp1 = tmp1.next
                else:
                    tmp.next = tmp2
                    tmp = tmp.next
                    tmp2 = tmp2.next
            if tmp1:
                tmp.next = tmp1
            elif tmp2:
                tmp.next = tmp2
            return dummy.next
        length = 0
        tmp = head
        while tmp:
            length+=1
            tmp=tmp.next
        dummy = ListNode(0,head)
        subLength = 1
        while subLength < length:
            pre, curr = dummy, dummy.next
            while curr:
                head1 = curr
                for i in range(1,subLength):
                    if curr.next:
                        curr=curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr=head2
                for i in range(1,subLength):
                    if curr and curr.next:
                        curr=curr.next
                    else:
                        break
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                tmpmeg = merge(head1,head2)
                pre.next = tmpmeg
                while pre.next:
                    pre = pre.next
                curr = succ
            subLength<<=1
        return dummy.next

                 
