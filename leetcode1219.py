# 1219. 黄金矿工
# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

# 为了使收益最大化，矿工需要按以下规则来开采黄金：

# 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
# 矿工每次可以从当前位置向上下左右四个方向走。
# 每个单元格只能被开采（进入）一次。
# 不得开采（进入）黄金数目为 0 的单元格。
# 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-with-maximum-gold
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        diff = [(-1,0),(1,0),(0,1),(0,-1)]
        m,n = len(grid),len(grid[0])
        ans = 0
        def dfs(i,j,count,visited):
            nonlocal ans
            for x,y in diff:
                nx = i+x
                ny = j+y
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny]!=0:
                    visited.add((nx,ny))
                    dfs(nx,ny,count+grid[nx][ny],visited)
                    visited.remove((nx,ny))
            ans = max(count,ans)
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    visited = set()
                    visited.add((i,j))
                    dfs(i,j,grid[i][j],visited)
        return ans

sol = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(sol.getMaximumGold(grid))
        
        
                