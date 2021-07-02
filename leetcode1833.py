# 1833. 雪糕的最大数量
# 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。

# 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。

# 给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。

# 注意：Tony 可以按任意顺序购买雪糕。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-ice-cream-bars
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        pre = [0]
        for cost in costs:
            pre.append(pre[-1]+cost)
        ind = bisect.bisect_right(pre,coins)
        return ind-1


class Solution2:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if cost>coins:
                break
            coins -=cost
            res+=1
        return res
    

costs = [10,6,8,7,7,8]
coins = 5
sol = Solution()
print(sol.maxIceCream(costs,coins))