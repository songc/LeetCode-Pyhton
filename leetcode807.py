# 807. 保持城市天际线
# 在二维数组grid中，grid[i][j]代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0 也被认为是建筑物。

# 最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的“天际线”必须与原始数组的天际线相同。 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。

# 建筑物高度可以增加的最大总和是多少？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxY = [max(x) for x in grid]
        maxX = []
        m,n = len(grid),len(grid[0])
        for j in range(n):
            tmp = []
            for i in range(m):
                tmp.append(grid[i][j])
            maxX.append(max(tmp))
        res=0
        for i in range(m):
            for j in range(n):
                res+=min(maxX[j],maxY[i])-grid[i][j]
        return res

sol = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(sol.maxIncreaseKeepingSkyline(grid))
