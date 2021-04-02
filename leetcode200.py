# 200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        parent = [i for i in range(m*n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
    
        def union(x,y):
            parent[find(y)]=find(x)

        count0 = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    x = i*n+j
                    if i+1<m and grid[i+1][j]=="1":
                        y = (i+1)*n+j
                        union(x,y)
                    if j+1<n and grid[i][j+1]=="1":
                        y = i*n+j+1
                        union(x,y)
                else:
                    count0+=1
        vset = set()
        for i in range(len(parent)):
            vset.add(find(i))
        return len(vset)-count0

sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid))