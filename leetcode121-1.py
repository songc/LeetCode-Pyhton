import collections
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        tmpMin = prices[0]
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1],prices[i]-tmpMin)
            if prices[i]<tmpMin:
                tmpMin=prices[i]
        return dp[-1]
        
