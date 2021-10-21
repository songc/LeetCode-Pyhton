# 295. 数据流的中位数
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

# 例如，

# [2,3,4] 的中位数是 3

# [2,3] 的中位数是 (2 + 3) / 2 = 2.5

# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-median-from-data-stream
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import bisect
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []


    def addNum(self, num: int) -> None:
        bisect.insort_right(self.data,num)


    def findMedian(self) -> float:
        n = len(self.data)
        div,mod = divmod(n,2)
        if mod==0:
            return (self.data[div-1]+self.data[div])/2.0
        else:
            return self.data[div]

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smailHp = []
        self.bigHp = [] 


    def addNum(self, num: int) -> None:
        if len(self.bigHp)==0:
            self.bigHp.append(-num)
            return
        if len(self.bigHp)==len(self.smailHp):
            if num< -self.bigHp[0]:
                heapq.heappush(self.bigHp,-num)
            else:
                heapq.heappush(self.bigHp,-heapq.heappushpop(self.smailHp,num))
        else:
            if num<-self.bigHp[0]:
                heapq.heappush(self.smailHp,-heapq.heappushpop(self.bigHp,-num))
            else:
                heapq.heappush(self.smailHp,num)
        

    def findMedian(self) -> float:
        if len(self.bigHp)>len(self.smailHp):
            return -self.bigHp[0]
        else:
            return (-self.bigHp[0]+self.smailHp[0])/2

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
obj.addNum(3)
obj.addNum(4)
param_2 = obj.findMedian()