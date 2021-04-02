# 234. 回文链表
# 请判断一个链表是否为回文链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        tmp = head
        while tmp:
            nodes.append(tmp)
            tmp=tmp.next
        left,right = 0,len(nodes)-1
        while left<right:
            if nodes[left].val != nodes[right].val:
                return False
            left+=1
            right-=1
        return True

def createListNode(lists:list):
    dummy = ListNode(0,None)
    tmp = dummy
    for i in lists:
        tmp.next=ListNode(i)
        tmp=tmp.next
    return dummy.next

sol = Solution()
nums = [1,2,2,1]
print(sol.isPalindrome(createListNode(nums)))