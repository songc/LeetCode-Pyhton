# 638. 大礼包
# 在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

# 给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中 needs[i] 是需要购买第 i 件物品的数量。

# 还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第 j 件物品的数量，且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。

# 返回 确切 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shopping-offers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 贪心，不对有问题
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        discords = []
        n = len(price)
        for spe in special:
            tmp = 0
            for i in range(n):
                tmp += price[i]*spe[i]
            if tmp>0:
                discords.append([tmp-spe[n]]+spe)
        discords.sort()
        res = 0
        while discords:
            flag = True
            for i in range(n):
                if needs[i]<discords[-1][i+1]:
                    flag=False
                    break
            if flag:
                for i in range(n):
                    needs[i]-=discords[-1][i+1]
                res+=discords[-1][-1]
            else:
                discords.pop()
        for i in range(n):
            res+=needs[i]*price[i]
        return res

from functools import lru_cache
class Solution2:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filterSpecial = []
        n = len(price)
        for spe in special:
            tmp = 0
            for i in range(n):
                tmp += price[i]*spe[i]
            if tmp>0:
                filterSpecial.append(spe)
        
        @lru_cache()
        def dfs(curNeed):
            minSum = sum(price[i]*curNeed[i] for i in range(n))
            for fspe in filterSpecial:
                nextNeed = []
                for i in range(n):
                    if curNeed[i]>=fspe[i]:
                        nextNeed.append(curNeed[i]-fspe[i])
                if len(nextNeed)==n:
                    minSum = min(minSum,dfs(tuple(nextNeed))+fspe[-1])
            return minSum
        return dfs(tuple(needs))
                        
                





sol = Solution2()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(sol.shoppingOffers(price,special,needs))



