# 827. 最大人工岛
# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。

# 返回执行此操作后，grid 中最大的岛屿面积是多少？

# 岛屿 由一组上、下、左、右四个方向相连的 1 形成。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/making-a-large-island
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = list(range(n*n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX<rootY:
                parent[rootY]=rootX
            else:
                parent[rootX]=rootY
        diff = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                ind = i*n+j
                for dx,dy in diff:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                        union(ind,nx*n+ny)
        vdict = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    ind = i*n+j
                    r = find(ind)
                    vdict[r]+=1
        if len(vdict)>0:
            ans = max(vdict[x] for x in vdict)
        else:
            ans = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    continue
                tmp = set()
                for dx,dy in diff:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                        tmp.add(find(nx*n+ny))
                ans = max(ans,sum(vdict[t] for t in tmp)+1)
        return ans


sol = Solution()
grid = [[1, 1], [1, 1]]
print(sol.largestIsland(grid))
