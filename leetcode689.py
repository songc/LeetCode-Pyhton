# 689. 三个无重叠子数组的最大和
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。

# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1]+i)
        dp=[[0]*4 for _ in range(n+5)]
        for i in range(n-k+1,0,-1):
            for j in range(1,4):
                dp[i][j]=max(dp[i+1][j],dp[i+k][j-1]+preSum[i+k-1]-preSum[i-1])
        res = []
        i,j = 1,3
        while j>0:
            if dp[i+1][j]>dp[i+k][j-1]+preSum[i+k-1]-preSum[i-1]:
                i+=1
            else:
                res.append(i-1)
                i+=k
                j-=1
        return res

sol = Solution()
nums = [1,2,1,2,6,7,5,1]
k = 2
print(sol.maxSumOfThreeSubarrays(nums,k))
