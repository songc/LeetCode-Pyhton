# 1034. 边界着色
# 给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

# 当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一 连通分量 。

# 连通分量的边界 是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。

# 请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coloring-a-border
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        parent = [i for i in range(m*n)]
        def findParent(x):
            if parent[x]!=x:
                parent[x]=findParent(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx=findParent(x)
            rooty=findParent(y)
            if rootx!=rooty:
                parent[rooty]=rootx
        diff = [(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                for dx,dy in diff:
                    nx = i+dx
                    ny = j+dy
                    if nx>=0 and ny>=0:
                        if grid[i][j]==grid[nx][ny]:
                            union(i*n+j,nx*n+ny)
        rootTarget = findParent(row*n+col)
        diff = [(0,-1),(0,1),(1,0),(-1,0)]
        for i in range(m*n):
            tp = findParent(i)
            if tp==rootTarget:
                x,y = divmod(i,n)
                if x==0 or x==m-1 or y==0 or y==n-1:
                    grid[x][y]=color
                else:
                    for dx,dy in diff:
                        nx=x+dx
                        ny=y+dy
                        if 0<=nx<m and 0<=ny<n:
                            if findParent(nx*n+ny)!=rootTarget:
                                grid[x][y]=color
        return grid

sol = Solution()
grid = [[1,1,1],[1,1,1],[1,1,1]]
row = 1
col = 1
color = 2
print(sol.colorBorder(grid,row,col,color))