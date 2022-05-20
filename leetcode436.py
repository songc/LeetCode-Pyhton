# 436. 寻找右区间
# 给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

# 区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

# 返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-right-interval
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from bisect import bisect, bisect_left
from code import interact
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startMap = dict()
        for i,v in enumerate(intervals):
            startMap[v[0]]=i
        startList = sorted(startMap.keys())
        ans = []
        for s,e in intervals:
            ind = bisect_left(startList,e)
            if ind==len(startList):
                ans.append(-1)
            else:
                ans.append(startMap[startList[ind]])
        return ans

sol = Solution()
intervals = [[3,4],[2,3],[1,2]]
print(sol.findRightInterval(intervals))