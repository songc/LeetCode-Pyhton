# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1,1,2]
        for i in range(3,n+1):
            dp.append(dp[-1]+dp[-2])
        return dp[n]

sol = Solution()
print(sol.climbStairs(1))