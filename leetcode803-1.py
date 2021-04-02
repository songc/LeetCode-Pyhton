class Solution:
    def hitBricks(self, grid: list, hits: list) -> list:
        res=[]
        m,n = len(grid),len(grid[0])
        cell=(-1,-1)
        parent=dict()
        parent[cell]=cell
        count=dict()
        count[cell]=1
        rank=dict()
        rank[cell]=0
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootX= find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX]<rank[rootY]:
                    parent[rootX]=rootY
                    count[rootY]+=count[rootX]
                    rank[rootY]+=1
                else:
                    parent[rootY]=rootX
                    count[rootX]+=count[rootY]
                    rank[rootX]+=1
        def megerNei(x,y):
            if x-1>=0 and grid[x-1][y]==1:
                union((x,y),(x-1,y))
            if x+1<m and grid[x+1][y]==1:
                union((x,y),(x+1,y))
            if y+1<n and grid[x][y+1]==1:
                union((x,y),(x,y+1))
            if y-1>=0 and grid[x][y-1]==1:
                union((x,y),(x,y-1))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    parent[(i,j)]=(i,j)
                    count[(i,j)]=1
                    rank[(i,j)]=0
        for x,y in hits:
            grid[x][y] -= 1

        for j in range(n):
            if grid[0][j]==1:
                union(cell,(0,j))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    megerNei(i,j)
        
        for x,y in hits[::-1]:
            grid[x][y]+=1
            if grid[x][y] !=1:
                res.append(0)
                continue
            befSize = count[find(cell)]
            megerNei(x,y)
            if x ==0:
                union(cell,(x,y))

            afterSize = count[find(cell)]
            size=afterSize-befSize-1
            if size>0:
                res.append(size)
            else:
                res.append(0)
        res.reverse()
        return res

sol=Solution()
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
print(sol.hitBricks(grid,hits))


        

        