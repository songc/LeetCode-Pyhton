
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = [0]*n
        buy = [0]*n
        cool = [0]*n
        buy[0] = -prices[0]
        for i in range(1,n):
            sell[i]=max(sell[i-1],buy[i-1]+prices[i])
            buy[i]=max(buy[i-1],cool[i-1]-prices[i])
            cool[i]=max(cool[i-1],sell[i-1])

        return max(sell[-1],cool[-1])

sol = Solution()
prices= [1,2,4,7,11]
print(sol.maxProfit(prices))
