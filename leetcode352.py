# 352. 将数据流变为多个不相交区间
#  给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

# 实现 SummaryRanges 类：

# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
import bisect
from typing import List

class SummaryRanges:

    def __init__(self):
        self.intervals = [[-10,-10],[100000,100000]]



    def addNum(self, val: int) -> None:
        tmp = [val,val]
        ind = bisect.bisect_right(self.intervals,tmp)
        if self.intervals[ind-1][1]>=val:
            return
        if self.intervals[ind-1][1]==val-1:
            if self.intervals[ind][0]==val+1:
                self.intervals[ind-1][1]=self.intervals[ind][1]
                self.intervals.pop(ind)
            else:
                self.intervals[ind-1][1]=val
            return 
        if self.intervals[ind][0] == val+1 or self.intervals[ind][0]==val:
            self.intervals[ind][0]=val
            return
        self.intervals.insert(ind,tmp)
        
        


    def getIntervals(self) -> List[List[int]]:
        return self.intervals[1:-1]



# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(6)
obj.addNum(6)
param_2 = obj.getIntervals()