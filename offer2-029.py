# 剑指 Offer II 029. 排序的循环链表
# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。

# 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

# 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

# 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/4ueAj6
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if head is None:
            newNode.next=newNode
            return newNode
        tmp = head
        if tmp.next==tmp:
            newNode.next=tmp.next
            tmp.next=newNode
            return head
        while tmp:
            if tmp.val<=insertVal and tmp.next.val>=insertVal or (tmp.val>tmp.next.val and (tmp.val<insertVal or tmp.next.val>insertVal)):
                newNode.next=tmp.next
                tmp.next=newNode
                break
            else:
                if tmp.next==head:
                    newNode.next=tmp.next
                    tmp.next=newNode
                    break
                else:
                    tmp=tmp.next
                
        return head
            