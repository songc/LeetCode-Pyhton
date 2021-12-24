# 1705. 吃苹果的最大数目
# 有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。

# 你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。

# 给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-eaten-apples
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(days)
        res=0
        deque = []
        day = 0
        while deque or day<n:
            if day<n and apples[day]>0:
                heapq.heappush(deque,[day+days[day],apples[day]])
            while deque and (deque[0][0]<=day or deque[0][1]==0):
                heapq.heappop(deque)
            if deque:
                deque[0][1]-=1
                res+=1
            day+=1
        return res

sol = Solution()
apples = [1,2,3,5,2]
days = [3,2,1,4,2]
print(sol.eatenApples(apples,days))