# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def createListNode(lists:list):
    dummy = ListNode(0,None)
    tmp = dummy
    for i in lists:
        tmp.next=ListNode(i)
        tmp=tmp.next
    return dummy.next