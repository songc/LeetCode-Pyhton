# 494. 目标和
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/target-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def backtrack(nums,begin,cursum):
            if begin>=len(nums):
                if cursum==S:
                    return 1
                return 0
            x = backtrack(nums,begin+1,cursum+nums[begin])
            y = backtrack(nums,begin+1,cursum-nums[begin])
            return x+y
        return backtrack(nums,0,0)

import collections
class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp=collections.defaultdict(dict)
        n = len(nums)
        one = nums[0]
        dp[0][one]=dp[0].get(one,0)+1
        dp[0][-one]=dp[0].get(-one,0)+1
        for i in range(1,n):
                for key in dp[i-1]:
                    dp[i][key+nums[i]]=dp[i].get(key+nums[i],0)+dp[i-1][key]
                    dp[i][key-nums[i]]=dp[i].get(key-nums[i],0)+dp[i-1][key]
        return dp[n-1].get(S,0)
nums= [1,1,1,1,1,1]
S= 3
sol = Solution2()
print(sol.findTargetSumWays(nums,S))