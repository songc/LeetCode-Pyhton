# 剑指 Offer II 091. 粉刷房子
# 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

# 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。

# 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。

# 请计算出粉刷完所有房子最少的花费成本。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/JEj789
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp=costs[0]
        for i in range(1,len(costs)):
            tmp = [0,0,0]
            tmp[0]=min(dp[1],dp[2])+costs[i][0]
            tmp[1]=min(dp[0],dp[2])+costs[i][1]
            tmp[2]=min(dp[0],dp[1])+costs[i][2]
            dp=tmp
        return min(dp)

sol = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(sol.minCost(costs))