# 641. 设计循环双端队列
# 设计实现双端队列。

# 实现 MyCircularDeque 类:

# MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
# boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
# boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
# boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
# boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
# int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
# int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
# boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
# boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/design-circular-deque
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class MyCircularDeque:

    def __init__(self, k: int):
        self.len = k
        self.cnt=[None]*(k+1)
        self.head = 0
        self.tail = 0


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head=(self.head+self.len)%(self.len+1)
        self.cnt[self.head]=value
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cnt[self.tail]=value
        self.tail=(self.tail+1)%(self.len+1)
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head=(self.head+1)%(self.len+1)
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail=(self.tail+self.len)%(self.len+1)
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.cnt[self.head]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cnt[self.tail-1]


    def isEmpty(self) -> bool:
        return self.tail==self.head


    def isFull(self) -> bool:
        return (self.tail+1)%(self.len+1)==self.head




# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()