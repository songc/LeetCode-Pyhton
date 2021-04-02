# 1579. 保证图可完全遍历
# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

# 类型 1：只能由 Alice 遍历。
# 类型 2：只能由 Bob 遍历。
# 类型 3：Alice 和 Bob 都可以遍历。
# 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

# 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list) -> int:
        ans = 0
        parentA=[i for i in range(n+1)]
        parentB=[i for i in range(n+1)]
        def find(x, parent):
            if parent[x]!=x:
                parent[x]=find(parent[x],parent)
            return parent[x]
        sordEdges = sorted(edges,key=lambda x:x[0])
        while sordEdges:
            type1, v1, v2 = sordEdges.pop()
            if type1==3:
                rootAV1 = find(v1, parentA)
                rootAV2 = find(v2, parentA)
                rootBV1 = find(v1, parentB)
                rootBV2 = find(v2, parentB)
                if rootAV1 != rootAV2:
                    parentA[rootAV2]=rootAV1
                if rootBV1 != rootBV2:
                    parentB[rootBV2]=rootBV1
                else:
                    ans+=1
            if type1 == 2:
                rootAV1 = find(v1, parentA)
                rootAV2 = find(v2, parentA)
                if rootAV1 != rootAV2:
                    parentA[rootAV2]=rootAV1
                else:
                    ans+=1
            if type1 ==1 :
                rootBV1 = find(v1, parentB)
                rootBV2 = find(v2, parentB)
                if rootBV1 != rootBV2:
                    parentB[rootBV2]=rootBV1
                else:
                    ans+=1
        rootA = set()
        rootB = set()
        for i in range(n+1):
            rootA.add(find(i,parentA))
            rootB.add(find(i,parentB))
        if len(rootA)>2 or len(rootB)>2:
            return -1
        return ans

sol = Solution()
n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
print(sol.maxNumEdgesToRemove(n,edges))