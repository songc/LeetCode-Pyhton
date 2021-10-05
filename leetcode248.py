# 284. 窥探迭代器
# 请你设计一个迭代器，除了支持 hasNext 和 next 操作外，还支持 peek 操作。

# 实现 PeekingIterator 类：

# PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
# int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
# bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
# int peek() 返回数组中的下一个元素，但 不 移动指针。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/peeking-iterator
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cnt = []
        while iterator.hasNext():
            self.cnt.append(iterator.next())
        self.curr = 0
        self.maxInd = len(self.cnt)
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cnt[self.curr]
        

    def next(self):
        """
        :rtype: int
        """
        while self.hasNext():
            res = self.peek()
            self.curr+=1
            return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr<self.maxInd

class PeekingIterator2:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._hasNext = iterator.hasNext()
        self._next = iterator.next() 
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        

    def next(self):
        """
        :rtype: int
        """
        res = self._next
        self._hasNext = self.iterator.hasNext()
        if self._hasNext:
            self._next=self.iterator.next()
        else:
            self._next = None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._hasNext

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].