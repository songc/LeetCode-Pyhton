# 430. 扁平化多级双向链表
# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

# 给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.flattendfs(head)
        return head

    
    def flattendfs(self, head: 'Node'):
        if not head:
            return head
        tmp = head
        while tmp.next or tmp.child:
            if tmp.child:
                mh,ml = self.flattendfs(tmp.child)
                ml.next = tmp.next
                tmp.next = mh
                mh.prev = tmp
                tmp.child = None
                if ml.next:
                    ml.next.prev=ml
                tmp=ml
                continue
            tmp=tmp.next
        return head,tmp

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.dfs(head)
        return head

    
    def dfs(self, head: 'Node'):
        tmp = head
        last = None
        while tmp:
            nt = tmp.next
            if tmp.child:
                ml = self.dfs(tmp.child)
                ml.next = nt
                tmp.next = tmp.child
                tmp.child.prev = tmp
                tmp.child = None
                if nt:
                    nt.prev=ml
                last = ml
            else:
                last = tmp
            tmp=nt
        return last