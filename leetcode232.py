# 232. 用栈实现队列

# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：

# 实现 MyQueue 类：

# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
 

# 说明：

# 你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

# 进阶：

# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inOrder = []
        self.reOrder = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.reOrder:
            self.inOrder.append(self.reOrder.pop())
        self.inOrder.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.inOrder)>1:
            self.reOrder.append(self.inOrder.pop())
        if self.inOrder:
            return self.inOrder.pop()
        return self.reOrder.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.inOrder:
            return self.inOrder[0]
        if self.reOrder:
            return self.reOrder[-1]
        return None


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inOrder)==0 and len(self.reOrder)==0



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()

print(param_2,param_3,param_4)