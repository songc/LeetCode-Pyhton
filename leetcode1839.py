# 1893. 检查是否区域内所有整数都被覆盖
# 给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

# 如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

# 已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rangesSorted = sorted(ranges, key = lambda x:x[0])
        newRange = [rangesSorted[0]]
        n = len(rangesSorted)
        for i in range(1,n):
            if rangesSorted[i][0]>newRange[-1][1]+1:
                newRange.append(rangesSorted[i])
                continue
            if rangesSorted[i][1]>newRange[-1][1]:
                newRange[-1][1]=rangesSorted[i][1]
        for start,end in newRange:
            if start<=left and end>=right:
                return True
        return False

class Solution2:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0]*52
        for l,r in ranges:
            diff[l]+=1
            diff[r+1]-=1
        preSum=[diff[0]]
        for i in range(1,52):
            preSum.append(preSum[-1]+diff[i])
        for i in range(left,right+1):
            if preSum[i]<1:
                return False
        return True

sol = Solution2()
ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
# ranges = [[1,10],[10,20]]
# left = 21
# right = 21
print(sol.isCovered(ranges,left,right))