# LCP 07. 传递信息
# 小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：

# 有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
# 每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
# 每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
# 给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/chuan-di-xin-xi
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        vDict = collections.defaultdict(list)
        for b,e in relation:
            vDict[b].append(e)

        def dfs(begin, step, target):
            num = 0
            if step == k:
                if begin == target:
                    return 1
                else:
                    return 0 
            for end in vDict[begin]:
                num +=dfs(end,step+1,target)
            return num
        return dfs(0,0,n-1)

sol = Solution()
n = 5
relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
k = 3
print(sol.numWays(n,relation,k))
            

