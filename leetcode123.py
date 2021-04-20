# 123. 买卖股票的最佳时机 III

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
        