# 883. 三维形体投影面积
# 在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。

# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

# 现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。

# 投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

# 返回 所有三个投影的总面积 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = sum(max(i) for i in grid)
        m,n = len(grid),len(grid[0])
        y = 0
        for i in range(n):
            t=0
            for j in range(m):
                t = max(grid[j][i],t)
            y+=t
        z = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    z+=1
        return x+y+z

sol = Solution()
grid = [[1,2],[3,4]]
print(sol.projectionArea(grid))