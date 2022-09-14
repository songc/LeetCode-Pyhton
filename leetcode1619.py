# 1619. 删除某些元素后的数组均值
# 给你一个整数数组 arr ，请你删除最小 5% 的数字和最大 5% 的数字后，剩余数字的平均值。

# 与 标准答案 误差在 10-5 的结果都被视为正确结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/mean-of-array-after-removing-some-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        d = int(len(arr)*0.05)
        s = sum(arr[d:-d])
        return s/(len(arr)-2*d)

sol = Solution()
arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
print(sol.trimMean(arr))