# 815. 公交路线
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。

# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。

# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/bus-routes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        indRoute = collections.defaultdict(list)
        for i in range(len(routes)):
            for n in routes[i]:
                indRoute[n].append(i)
        visited = set()
        dist = collections.defaultdict(int)
        dist[source]=0
        def dfs(node, currNum):
            currNode = []
            for i in indRoute[node]:
                if i in visited:
                    continue
                for nd in routes[i]:
                    if nd not in dist:
                        dist[nd] = currNum+1
                        currNode.append(nd)
                visited.add(i)
            return currNode
        currNode = [source]
        count = 0
        while currNode:
            tmp = []
            for no in currNode:
                tmp.extend(dfs(no,count))
            count+=1
            currNode = tmp
            if target in dist:
                break                
        dfs(source,0)
        if target in dist:
            return dist[target]
        else:
            return -1

sol = Solution()
routes = [[0,1,6,16,22,23],[14,15,24,32],[4,10,12,20,24,28,33],[1,10,11,19,27,33],[11,23,25,28],[15,20,21,23,29],[29]]
source = 4
target = 21
print(sol.numBusesToDestination(routes,source,target))
                
                
        


