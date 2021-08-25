# 787. K 站中转内最便宜的航班
# 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 toi 抵达 pricei。

# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections
import bisect

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         flightsDict = collections.defaultdict(list)
#         for flight in flights:
#             flightsDict[flight[0]].append(flight)
#         visited=set()
#         distTarget = dict()
#         def bfs(nodes,num):
#             if num>k:
#                 return
#             nextNode = []
#             for node,cost in nodes:
#                 if node in visited:
#                     continue
#                 visited.add(node)
#                 for flight in flightsDict[node]:
#                     _, dst, c = flight
#                     if dst in distTarget:
#                         distTarget[dst]=min(distTarget[dst],cost+c)
#                     else:
#                         distTarget[dst]=cost+c
#                     if dst not in visited:
#                         nextNode.append((dst,distTarget[dst]))
#             bfs(nextNode,num+1)
#         bfs([(src,0)],0)
#         return distTarget[dst] if dst in distTarget else -1

# 费时，广度优先
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightsDict = collections.defaultdict(list)
        for flight in flights:
            flightsDict[flight[0]].append(flight)
        distTarget = [float('inf')]*n
        visited=dict()
        queue = collections.deque()
        queue.append([0,src,-1])
        while queue:
            cost,d,num = queue.popleft()
            if num>k:
                continue
            distTarget[d]=min(distTarget[d],cost)
            if d in visited and num>visited[d]:
                continue
            visited[d]=num
            for _, dt, c in flightsDict[d]:
                bisect.insort_right(queue,[cost+c,dt,num+1])
        return distTarget[dst] if distTarget[dst]!=float('inf') else -1

# 动态规划
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp=[[float('inf')]*(k+2) for _ in range(n)]
        dp[src][0]=0
        for i in range(1,k+2):
            for f,to,cost in flights:
                dp[to][i]=min(dp[to][i],dp[f][i-1]+cost)
        res = min(dp[dst])
        return  res if res != float('inf') else -1


sol = Solution2()
n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0
# n = 15
# edges = [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]]
# src = 1
# dst = 4
# k = 10
print(sol.findCheapestPrice(n,edges,src,dst,k))
                

