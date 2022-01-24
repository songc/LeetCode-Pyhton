# 2045. 到达目的地的第二短时间
# 城市用一个 双向连通 图表示，图中有 n 个节点，从 1 到 n 编号（包含 1 和 n）。图中的边用一个二维整数数组 edges 表示，其中每个 edges[i] = [ui, vi] 表示一条节点 ui 和节点 vi 之间的双向连通边。每组节点对由 最多一条 边连通，顶点不存在连接到自身的边。穿过任意一条边的时间是 time 分钟。

# 每个节点都有一个交通信号灯，每 change 分钟改变一次，从绿色变成红色，再由红色变成绿色，循环往复。所有信号灯都 同时 改变。你可以在 任何时候 进入某个节点，但是 只能 在节点 信号灯是绿色时 才能离开。如果信号灯是  绿色 ，你 不能 在节点等待，必须离开。

# 第二小的值 是 严格大于 最小值的所有值中最小的值。

# 例如，[2, 3, 4] 中第二小的值是 3 ，而 [2, 2, 4] 中第二小的值是 4 。
# 给你 n、edges、time 和 change ，返回从节点 1 到节点 n 需要的 第二短时间 。

# 注意：

# 你可以 任意次 穿过任意顶点，包括 1 和 n 。
# 你可以假设在 启程时 ，所有信号灯刚刚变成 绿色 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        dist=[[float('inf')]*2 for _ in range(n+1)]
        dist[1][0]=0
        deque = collections.deque()
        deque.append([1,0])
        while dist[n][1]== float('inf'):
            v,d = deque.popleft()
            d = d+1
            for y in graph[v]:
                if d<dist[y][0]:
                    dist[y][0]=d
                    deque.append([y,d])
                elif dist[y][0]<d<dist[y][1]:
                    dist[y][1]=d
                    deque.append([y,d])
        ans = 0
        tmp = 2*change
        for _ in range(dist[n][1]):
            mod = ans%tmp
            if mod>=change:
                ans+=tmp-mod
            ans+=time
        return ans

sol = Solution()
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
print(sol.secondMinimum(n,edges,time,change))