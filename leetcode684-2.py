import collections
class Solution:
    def findRedundantConnection(self, edges: list) -> list:
        v = set()
        for v1, v2 in edges:
            v.add(v1)
            v.add(v2)
        parent=[i for i in range(len(v)+1)]
        parent[0]=1
        def find(i):
            if parent[i]!=i:
                parent[i]=find(parent[i])
            return parent[i]
        def union(x,y):
            rX = find(x)
            rY = find(y)
            parent[rY]=parent[rX]
        for v1, v2 in  edges:
            r1 = find(v1)
            r2 = find(v2)
            if r1 != r2:
                parent[r2]=r1
            else:
                return [v1,v2]

sol=Solution()
edges=[[3,4],[1,2],[2,4],[3,5],[2,5]]
print(sol.findRedundantConnection(edges))