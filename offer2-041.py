# 剑指 Offer II 041. 滑动窗口的平均值
# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。

# 实现 MovingAverage 类：

# MovingAverage(int size) 用窗口大小 size 初始化对象。
# double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/qIsx9U
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.deque = collections.deque(maxlen=size)
        self.size = size
        self.count = 0
        self.sum = 0
        


    def next(self, val: int) -> float:
        if self.count<self.size:
            self.deque.append(val)
            self.sum+=val
            self.count+=1
        else:
            self.sum-=self.deque.popleft()
            self.deque.append(val)
            self.sum+=val
        return self.sum/self.count





# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)