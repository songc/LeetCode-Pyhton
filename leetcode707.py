# 707. 设计链表
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

# 在链表类中实现这些功能：

# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/design-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Node:
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head=Node()
        self.tail = Node()
        self.len = 0
        self.head.next=self.tail
        self.tail.pre=self.head

    def getNode(self, index: int) -> Node:
        if index<0 or index>=self.len:
            return None
        ans = self.head
        for _ in range(index+1):
            ans=ans.next
        return ans

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node:
            return node.val
        return -1


    def addAtHead(self, val: int) -> None:
        tmp = Node(val)
        tmp.next=self.head.next
        tmp.pre=self.head
        self.head.next.pre=tmp
        self.head.next=tmp
        self.len+=1


    def addAtTail(self, val: int) -> None:
        tmp = Node(val,self.tail.pre,self.tail)
        self.tail.pre.next=tmp
        self.tail.pre=tmp
        self.len+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index<=0:
            self.addAtHead(val)
        elif index<self.len:
            node = self.getNode(index)
            tmp = Node(val,node.pre,node)
            node.pre.next=tmp
            node.pre=tmp
            self.len+=1
        elif index == self.len:
            self.addAtTail(val)
        


    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        if node:
            node.pre.next= node.next
            node.next.pre = node.pre
            self.len-=1

obj = MyLinkedList()
param_1 = obj.get(0)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.deleteAtIndex(1)
param2 = obj.get(1)