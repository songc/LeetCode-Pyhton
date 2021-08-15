# 1583. 统计不开心的朋友
# 给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。

# 对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。

# 所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。

# 但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x 就会不开心：

# x 与 u 的亲近程度胜过 x 与 y，且
# u 与 x 的亲近程度胜过 u 与 v
# 返回 不开心的朋友的数目 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-unhappy-friends
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairDict = dict()

        for v1,v2 in pairs:
            pairDict[v1]=v2
            pairDict[v2]=v1
        res = [1]*n
        for i in range(n):
            tmp = pairDict[i]
            for v in preferences[i]:
                if v==tmp:
                    break
                tmp2 = pairDict[v]
                for j in preferences[v]:
                    if j==tmp2:
                        break
                    if j==i:
                        res[i]=0
                        break
                if res[i]==0:
                    break
        return n-sum(res)

sol = Solution()
n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
print(sol.unhappyFriends(n,preferences,pairs))

