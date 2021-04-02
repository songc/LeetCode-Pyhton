# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def merge(self, intervals: list) -> list:
        ans = []
        def add(interval):
            if len(ans)<1:
                ans.append(interval)
                return
            start,end = interval[0],interval[1]
            start1,end1 = ans[-1][0],ans[-1][1]
            if end1>=end:
                return
            if end1>=start:
                ans[-1]=[start1,end]
            if start>end1:
                ans.append(interval)
        for interval in sorted(intervals):
            add(interval)
        return ans

sol = Solution()
intervals=[[1,4],[4,5]]
print(sol.merge(intervals))
