# 1584. 连接所有点的最小费用

# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
class Solution:
    def minCostConnectPoints(self, points: list) -> int:
        visited=set()
        ans = 0
        n = len(points)
        if n==1:
            return 0
        distDict=collections.defaultdict(list)
        for i in range(n):
            for k in range(1,n):
                j = i+k
                if j>=n:
                    break
                x1,y1,x2,y2 = points[i][0], points[i][1],points[j][0],points[j][1]
                dis = abs(x2-x1)+abs(y2-y1)
                distDict[dis].append([i,j])
        dictList = sorted(distDict.keys())
        visited.update(distDict[dictList[0]][0])
        ans+=dictList[0]
        def dfs():
            for dis in dictList:
                for ind1,ind2 in distDict[dis]:
                    if ind1 in visited and ind2 in visited:
                        continue
                    if ind1 in visited or ind2 in visited:
                        visited.add(ind1)
                        visited.add(ind2)
                        return dis
                        
        while len(visited)<n:
            ans+=dfs()
        return ans

sol = Solution()
points=[[2,-3],[-17,-8],[13,8],[-17,-15]]
print(sol.minCostConnectPoints(points))
