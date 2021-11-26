# 847. 访问所有节点的最短路径
# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。

# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。

# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n==1:
            return 0
        target = 2**n-1
        visited = set()
        res = float('inf')
        queue = deque()
        for i in range(n):
            queue.append((i,1<<i,0))
            visited.add((i,1<<i))
        while queue:
            ind, mask, dist = queue.popleft()
            for nextInd in graph[ind]:
                nextMask = mask|(1<<nextInd)
                if nextMask==target:
                    res=min(res,dist+1)
                    continue
                if (nextInd, nextMask) in visited:
                    continue           
                queue.append((nextInd,nextMask,dist+1))
                visited.add((nextInd,nextMask))
        return res

class Solution2:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n==1:
            return 0
        target = 2**n-1
        visited = set()
        queue = deque()
        for i in range(n):
            queue.append((i,1<<i,0))
            visited.add((i,1<<i))
        while queue:
            ind, mask, dist = queue.popleft()
            if mask==target:
                return dist
            for nextInd in graph[ind]:
                nextMask = mask|(1<<nextInd)
                if (nextInd, nextMask) in visited:
                    continue           
                queue.append((nextInd,nextMask,dist+1))
                visited.add((nextInd,nextMask))
sol = Solution2()
graph = [[1,2,3],[0],[0],[0]]
print(sol.shortestPathLength(graph))