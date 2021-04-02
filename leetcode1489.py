# 1489. 找到最小生成树里的关键边和伪关键边
# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。

# 请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。

# 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。
import collections
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list) -> list:
        parent=[i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def init():
            for i in range(n):
                parent[i]=i
        def isTree():
            tree = find(0)
            for i in range(1,n):
                if find(i) != tree:
                    return False
            return True
        edgeDict = collections.defaultdict(list)
        for i in range(len(edges)):
            edgeDict[edges[i][-1]].append(edges[i]+[i])
        keySort = sorted(edgeDict.keys())
        minVal = 0
        for key in keySort:
            for edge in edgeDict[key]:
                rootX = find(edge[0])
                rootY = find(edge[1])
                if rootX!=rootY:
                    minVal+=key
                    parent[rootY]=rootX
        keyEdge=[]
        noKeyEdge=[]
        for i, testEdge in enumerate(edges):
            init()
            tmpVal=0
            for key in keySort:
                for edge in edgeDict[key]:
                    if edge[0]==testEdge[0] and edge[1]==testEdge[1]:
                        continue
                    rootX = find(edge[0])
                    rootY = find(edge[1])
                    if rootX!=rootY:
                        tmpVal+=key
                        parent[rootY]=rootX
            if isTree():
                if tmpVal==minVal:
                    noKeyEdge.append(i)
                elif tmpVal>minVal:
                    keyEdge.append(i)
            else:
                keyEdge.append(i)
        realNoKeyEdge=[]
        for ind in noKeyEdge:
            init()
            tmpVal=0
            v1=edges[ind][0]
            v2=edges[ind][1]
            tmpVal+=edges[ind][2]
            parent[find(v2)]=parent[find(v1)]
            for key in keySort:
                for edge in edgeDict[key]:
                    rootX = find(edge[0])
                    rootY = find(edge[1])
                    if rootX!=rootY:
                        tmpVal+=key
                        parent[rootY]=rootX
            if isTree():
                if tmpVal==minVal:
                    realNoKeyEdge.append(ind)
        
        return [keyEdge,realNoKeyEdge]

sol = Solution()
n = 4
edges=[[0,1,1],[0,3,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1]]
print(sol.findCriticalAndPseudoCriticalEdges(n,edges))

                        

        

