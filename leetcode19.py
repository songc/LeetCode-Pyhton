# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listNode = []
        tmp = head
        while tmp:
            listNode.append(tmp)
            tmp=tmp.next
        length = len(listNode)
        if n==0:
            return head
        elif n==1:
            if length==1:
                return None
            tmpNode = listNode[-2]
            tmpNode.next=None
            return listNode[0]
        elif n<length:
            lNode = listNode[-n-1]
            rNode = listNode[-n+1]
            lNode.next = rNode
            return listNode[0]
        elif n==length:
            return listNode[1]
