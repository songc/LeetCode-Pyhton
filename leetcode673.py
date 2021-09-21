# 673. 最长递增子序列的个数
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [1]*n
        dp2 = [0]*n
        dp2[0] = 1
        maxL = 1
        res = 0
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp1[i]=max(dp1[i],dp1[j]+1)
                    maxL=max(dp1[i],maxL)
        if maxL==1:
            return n
        for i in range(1,n):
            if dp1[i]==1:
                dp2[i]=1
                continue
            for j in range(i-1,-1,-1):
                if dp1[i]==dp1[j]+1 and nums[i]>nums[j]:
                    dp2[i]+=dp2[j]
        for i in range(n):
            if dp1[i]==maxL:
                res+=dp2[i]
        return res

sol = Solution()
nums = [3,1,2]
print(sol.findNumberOfLIS(nums))