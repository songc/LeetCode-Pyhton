# 155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-stack
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cnt = []
        self.tmin = None


    def push(self, x: int) -> None:
        self.cnt.append(x)
        if self.tmin is None:
            self.tmin = x
        else:
            if self.tmin>x:
                self.tmin=x



    def pop(self) -> None:
        x = self.cnt.pop()
        if x == self.tmin:
            if self.cnt:
                self.tmin = min(self.cnt)
            else:
                self.tmin = None


    def top(self) -> int:
        return self.cnt[-1]


    def getMin(self) -> int:
        return self.tmin



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()