# 797. 所有可能的路径
# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

# 二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。

# 译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/all-paths-from-source-to-target
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def backtrace(currNode,nodeList):
            nonlocal n
            if currNode == n-1:
                res.append(list(nodeList))
                return 
            for node in graph[currNode]:
                nodeList.append(node)
                backtrace(node,nodeList)
                nodeList.pop()
        backtrace(0,[0])
        return res

sol = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(sol.allPathsSourceTarget(graph))