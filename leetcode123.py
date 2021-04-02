class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n <=1:
            return 0
        buy=[-prices[0],-prices[0]]
        sell=[0,0]
        for i in range(1,n):
            buy[0]=max(buy[0],-prices[i])
            sell[0]=max(sell[0], prices[i]+buy[0])
            buy[1]=max(buy[1], sell[0]-prices[i])
            sell[1]=max(sell[1], prices[i]+buy[1])
        return max(sell)
        


sol= Solution()
prices = [1,2,4,2,5,7,2,4,9,0]
print(sol.maxProfit(prices))
        