# 1588. 所有奇数长度子数组的和
# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

# 子数组 定义为原数组中的一个连续子序列。

# 请你返回 arr 中 所有奇数长度子数组的和 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        preSum = [0]
        for i in arr:
            preSum.append(preSum[-1]+i)
        res = 0+preSum[-1]
        for i in range(3,n+1,2):
            for j in range(i,n+1):
                res+=preSum[j]-preSum[j-i]
        return res

sol = Solution()
arr = [1,4,2,5,3]
print(sol.sumOddLengthSubarrays(arr))