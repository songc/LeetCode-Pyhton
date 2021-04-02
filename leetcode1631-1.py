class Solution:
    def minimumEffortPath(self, heights: list) -> int:
        rows,cols = len(heights), len(heights[0])
        if rows==1 and cols==1:
            return 0
        parent=[i for i in range(rows*cols)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(y)]=find(x)
        edges=[]
        for i in range(rows):
            for j in range(cols):
                if i>0:
                    tmp = abs(heights[i][j]-heights[i-1][j])
                    edges.append([(i-1)*cols+j,i*cols+j,tmp])
                if j>0:
                    tmp = abs(heights[i][j]-heights[i][j-1])
                    edges.append([i*cols+j-1,i*cols+j,tmp])
        edgesorted = sorted(edges,key=lambda x:x[-1])
        for edge in edgesorted:
            union(edge[0],edge[1])
            if find(0)==find(rows*cols-1):
                return edge[-1]
sol = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(sol.minimumEffortPath(heights))