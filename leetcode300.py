# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        if n<=1:
            return n
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    if dp[i]>ans:
                        ans = dp[i]
                        break        
        return ans

sol = Solution()
nums = [0,1,0,3,2,3]
print(sol.lengthOfLIS(nums))
        
            