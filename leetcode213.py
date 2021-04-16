# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n<=3:
        #     return max(nums)
        # dp = [0]*n
        # dp2 = [False]*n
        # dp3 = [0]*n
        # dp[0]=nums[0]
        # dp2[0]=True
        # if nums[1]>=nums[0]:
        #     dp[1]=nums[1]
        # else:
        #     dp[1]=nums[0]
        #     dp2[1]=True
        # for i in range(2,n-1):
        #     tmp=nums[i]+dp[i-2]
        #     if tmp>=dp[i-1]:
        #         dp[i]=tmp
        #         dp2[i]=dp2[i-2]
        #     else:
        #         dp[i]=dp[i-1]
        #         dp2[i]=dp2[i-1]
        # dp[n-1]=dp[n-2]
        # for i in range(n-2,-1,-1):
        #     if not dp2[i]:
        #         dp[n-1]=max(dp[i]+nums[n-1],dp[n-2])
        #         break
        # return dp[-1]
        n = len(nums)
        dp0=[0]*(n-1)
        dp1=[0]*(n-1)
        dp0[0]=nums[0]
        dp0[1]=max(nums[0],nums[1])
        dp1[0]=nums[1]
        for i in range(2,n):
            if i<n-1:
                dp0[i]=max(dp0[i-2]+nums[i],dp0[i-1])
            dp1[i-1]=max(dp1[i-2],dp1[i-3]+nums[i])
        return max(dp1[-1],dp0[-1])



sol = Solution()
nums = [6,6,4,8,4,3,3,10]
print(sol.rob(nums))
        
        
