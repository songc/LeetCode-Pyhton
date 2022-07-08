# 1217. 玩筹码
# 有 n 个筹码。第 i 个筹码的位置是 position[i] 。

# 我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:

# position[i] + 2 或 position[i] - 2 ，此时 cost = 0
# position[i] + 1 或 position[i] - 1 ，此时 cost = 1
# 返回将所有筹码移动到同一位置上所需要的 最小代价 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from turtle import position
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ans = 2**32
        for i in position:
            tmp = 0
            for j in position:
                if abs(j-i)%2==1:
                    tmp+=1
            ans = min(tmp,ans)
        return ans

class Solution2:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a = 0
        b = 0
        for i in position:
            if i%2==0:
                a+=1
            else:
                b+=1
        return min(a,b)


sol = Solution()
position =[1,2,3]
print(sol.minCostToMoveChips(position))
