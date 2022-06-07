# 875. 爱吃香蕉的珂珂
# 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。

# 珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

# 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/koko-eating-bananas
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from bisect import bisect, bisect_right
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==1:
            return (piles[0]+h-1)//h
        piles.sort()
        if h==len(piles):
            return piles[-1]
        
        left = 1
        right = piles[-1]
        while left<right:
            mid = (left+right)//2
            target = self.getNum(piles,mid)
            if target>h:
                left=mid+1
            elif target<=h:
                right=mid
        return left


    def getNum(self,piles,h):
        ans = 0
        for pile in piles:
            ans+=(pile+h-1)//h
        return ans

sol = Solution()
piles = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]

h = 823855818
print(sol.minEatingSpeed(piles,h))