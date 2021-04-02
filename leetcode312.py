# 312. 戳气球
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

# 求所能获得硬币的最大数量。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/burst-balloons
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        def bestRange(i,j):
            b = 0
            for k in range(i+1,j):
                left = dp[i][k]
                right = dp[k][j]
                ans = left+right+nums[i]*nums[k]*nums[j]
                b = max(ans,b)
            dp[i][j]=b
        dp = [[0]*n for _ in range(n)]
        for k in range(2,n):
            for i in range(0,n-k):
                j = i+k
                bestRange(i,j)
        return dp[0][n-1]

sol = Solution()
nums = [3,1,5,8]
print(sol.maxCoins(nums))
