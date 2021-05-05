# 740. 删除并获得点数
# 给你一个整数数组 nums ，你可以对它进行一些操作。

# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-and-earn
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        ele = list(counter)
        ele.sort()
        n = len(ele)
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=ele[0]*counter[ele[0]]
        for i in range(2,n+1):
            if ele[i-2]==ele[i-1]-1:
                dp[i]=max(dp[i-1],dp[i-2]+ele[i-1]*counter[ele[i-1]])
            else:
                dp[i]=dp[i-1]+ele[i-1]*counter[ele[i-1]]
        return dp[-1]

sol = Solution()
nums = [2,2,3,3,3,4]
print(sol.deleteAndEarn(nums))