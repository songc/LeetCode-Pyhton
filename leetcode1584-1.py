import collections
class Solution:
    def minCostConnectPoints(self, points: list) -> int:
        ans = 0
        n = len(points)
        if n==1:
            return 0
        parent = [i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootX=find(x)
            rootY=find(y)
            parent[rootY]=rootX

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
        for dis in dictList:
            for ind1,ind2 in distDict[dis]:
                rootX = find(ind1)
                rootY = find(ind2)
                if rootX!=rootY:
                    parent[rootY]=rootX
                    ans+=dis
        return ans

sol = Solution()
points=[[2,-3],[-17,-8],[13,8],[-17,-15]]
print(sol.minCostConnectPoints(points))
