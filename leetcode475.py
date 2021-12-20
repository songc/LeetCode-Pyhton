# 475. 供暖器
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

# 在加热器的加热半径范围内的每个房屋都可以获得供暖。

# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/heaters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        res = 0
        ind = bisect.bisect_right(heaters,houses[0])
        for i in houses:
            while ind<n and i>heaters[ind]:
                ind+=1
            if ind==0:
                res=max(res,abs(i-heaters[ind]))
                continue
            if ind==n:
                res=max(res,abs(i-heaters[ind-1]))
                continue
            res=max(res,min(i-heaters[ind-1],heaters[ind]-i))
        return res
            

sol = Solution()
houses = [1,1,1,1,1,1,999,999,999,999,999]
heaters = [499,500,501]
# houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# heaters= [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
print(sol.findRadius(houses,heaters))
        