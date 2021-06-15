# 518. 零钱兑换 II
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0]=1
        # for i in range(1,amount+1):
        #     for j in range(0,n):
        #         if coins[j]<=i:
        #             dp[i]=dp[i]+dp[i-coins[j]]
        for j in range(0,n):
            for i in range(1,amount+1):
                if coins[j]<=i:
                     dp[i]=dp[i]+dp[i-coins[j]]
        return dp[-1]



sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.change(amount,coins))

