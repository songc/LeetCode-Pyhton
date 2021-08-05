# 802. 找到最终的安全状态
# 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。

# 对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。

# 返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。

# 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-eventual-safe-states
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vDict = dict()
        visted = set()
        def dfs(node):
            if node in vDict:
                return vDict[node]
            if node in visted:
                return False
            nodeList = graph[node]
            if not nodeList:
                vDict[node]=True
                return vDict[node]
            visted.add(node)
            for n in nodeList:
                flag = dfs(n)
                if not flag:
                    vDict[node]=False
                    return False
            visted.remove(node)
            vDict[node]=True
            return True
        res = []
        for i in range(len(graph)):
            flag = dfs(i)
            if flag:
                res.append(i)
        return res


class Solution2:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vList =[[] for _   in range(len(graph))]
        for ind, nodes in enumerate(graph):
            for n in nodes:
                vList[n].append(ind)
        degree = [len(nodes) for nodes in graph]
        vSet = set()
        deque = collections.deque((i for i, v in enumerate(degree) if v==0))
        while deque:
            v = deque.popleft()
            vSet.add(v)
            for n in vList[v]:
                degree[n]-=1
                if degree[n]==0:
                    deque.append(n)
        res = [i for i in range(len(vList)) if i in vSet]
        return res

sol = Solution2()
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(sol.eventualSafeNodes(graph))
        
        
