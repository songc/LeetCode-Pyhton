# 846. 一手顺子
# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

# 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hand-of-straights
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize>0:
            return False
        vdict = collections.defaultdict(int)
        keys=set()
        for i in hand:
            vdict[i]+=1
            keys.add(i)
        sortedkey = sorted(keys)
        while sortedkey:
            begin = sortedkey[0]
            count=0
            while count<groupSize:
                if begin in vdict:
                    vdict[begin]-=1
                else:
                    return False
                if vdict[begin]==0:
                    if begin==sortedkey[0]:
                        sortedkey.pop(0)
                    else:
                        return False
                begin+=1
                count+=1
        return True

sol = Solution()
hand = [1,2,3,4,5]
groupSize = 4
print(sol.isNStraightHand(hand,groupSize))


        
