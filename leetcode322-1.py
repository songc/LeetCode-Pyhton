from typing import List
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                ind = i-coin
                if ind>=0 and dp[ind]!=-1:
                    if dp[i]==-1:
                        dp[i]=dp[ind]+1
                    else:
                        if dp[ind]+1<dp[i]:
                            dp[i]=dp[ind]+1
        return dp[-1]

sol = Solution()
coins = [2,5,1]

amount = 11

print(sol.coinChange(coins,amount))
                    