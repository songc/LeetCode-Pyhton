# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        deque = collections.deque()
        for price in prices:
            while deque:
                if price<deque[-1]:
                    deque.pop()
                else:
                    deque.append(price)
                    ans = max(ans,deque[-1]-deque[0])
                    break
            if not deque:
                deque.append(price)
        return ans

            