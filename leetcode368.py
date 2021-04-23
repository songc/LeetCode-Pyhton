# 368. 最大整除子集
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-divisible-subset
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<=1:
            return nums
        dp=[1]*n
        ind=[i for i in range(n)]
        nums.sort()
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]%nums[j]==0:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        ind[i]=j
        maxVal = max(dp)
        ans=[]
        for i in range(n-1,-1,-1):
            if dp[i]!=maxVal:
                continue
            ans.append(nums[i])
            tmp = i
            while ind[tmp]!=tmp:
                ans.append(nums[ind[tmp]])
                tmp = ind[tmp]
            break                
        return ans

sol = Solution()
nums = [5,9,18,54,108,540,90,180,360,720]
print(sol.largestDivisibleSubset(nums))
                
