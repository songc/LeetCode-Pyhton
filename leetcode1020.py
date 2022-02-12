# 1020. 飞地的数量
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-enclaves
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        flag = m*n
        parent=[i for i in range(m*n+1)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            xr = find(x)
            yr = find(y)
            if xr==flag or yr ==flag:
                parent[xr]=flag
                parent[yr]=flag
            else:
                parent[xr]=yr
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                if i==0 or i==m-1 or j==0 or j==n-1:
                    parent[i*n+j]=flag
                if j>0 and grid[i][j-1]==1:
                    union(i*n+j,i*n+j-1)
                if i>0 and grid[i-1][j]==1:
                    union(i*n+j,i*n-n+j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and find(i*n+j)!=flag:
                    ans+=1
        return ans
sol = Solution()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(sol.numEnclaves(grid))

