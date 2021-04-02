# 309. 最佳买卖股票时机含冷冻期
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp=dict()
        for i in range(n):
            dp[i]=0
        dp[-1]=0
        dp[-2]=0
        ans = 0
        dp2 = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i==j:
                    dp2[i][j]=prices[i]
                else:
                    dp2[i][j]=min(dp2[i][j-1],prices[j])

        for i in range(1,n):
            if i==1:
                dp[i]=prices[1]-prices[0]
            elif i==2:
                dp[i]=prices[2]-min(prices[:2])
            elif i==3:
                dp[i]=prices[3]-min(prices[:3])
            else:
                for j in range(-1,i-1):
                    dp[i]=max(dp[i],dp[j-1]+prices[i]- dp2[j+1][i-1])
            ans = max(dp[i],ans)
        return ans

sol = Solution()
prices= [1,2,4,7,11]
print(sol.maxProfit(prices))
