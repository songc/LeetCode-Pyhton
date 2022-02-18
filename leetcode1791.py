# 1791. 找出星型图的中心节点
# 有一个无向的 星型 图，由 n 个编号从 1 到 n 的节点组成。星型图有一个 中心 节点，并且恰有 n - 1 条边将中心节点与其他每个节点连接起来。

# 给你一个二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间存在一条边。请你找出并返回 edges 所表示星型图的中心节点。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-center-of-star-graph
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vdict = collections.defaultdict(int)
        for u1,v1 in edges[:3]:
            vdict[u1]+=1
            vdict[v1]+=1
        u1,v1 =edges[0][0],edges[0][1]
        if vdict[u1]==3:
            return u1
        return v1


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        return edges[0][1] 


sol = Solution()
edges = [[1,2],[2,3],[4,2]]
print(sol.findCenter(edges))
