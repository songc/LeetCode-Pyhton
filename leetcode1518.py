# 1518. 换酒问题
# 小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

# 如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

# 请你计算 最多 能喝到多少瓶酒。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/water-bottles
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        tmp = numBottles
        while tmp>=numExchange:
            d,m = divmod(tmp,numExchange)
            res+=d
            tmp = m+d
        return res

class Solution2:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt,m = divmod(numBottles,numExchange-1)
        return cnt+numBottles-1 if m==0 else cnt+numBottles

sol = Solution2()
numBottles = 15
numExchange = 4
print(sol.numWaterBottles(numBottles,numExchange))