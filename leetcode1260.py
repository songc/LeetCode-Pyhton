# 1260. 二维网格迁移
# 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。

# 每次「迁移」操作将会引发下述活动：

# 位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
# 位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
# 位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
# 请你返回 k 次迁移操作后最终得到的 二维网格。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/shift-2d-grid
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp = n*i+j-k
                while tmp<0:
                    tmp+=m*n
                ans[i][j]=grid[tmp//n][tmp%n]
        return ans

sol = Solution()
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(sol.shiftGrid(grid,k))
