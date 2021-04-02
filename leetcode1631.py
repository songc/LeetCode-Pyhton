# 1631. 最小体力消耗路径
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

# 请你返回从左上角走到右下角的最小 体力消耗值 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-with-minimum-effort
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minimumEffortPath(self, heights: list) -> int:
        rows,cols = len(heights), len(heights[0])
        dp = [[float("inf")]*cols for _ in range(rows)]
        dp[0][0]=0
        def update(i,j):
            if i==0 and j==0:
                return
            if i>=1:
                tmp=abs(heights[i][j]-heights[i-1][j])
                tmp2 = max([tmp,dp[i-1][j]])
                dp[i][j]=min([tmp2,dp[i][j]])
            if i<rows-1:
                tmp=abs(heights[i][j]-heights[i+1][j])
                tmp2 = max([tmp,dp[i+1][j]])
                dp[i][j]=min([tmp2,dp[i][j]])
            if j>=1:
                tmp=abs(heights[i][j]-heights[i][j-1])
                tmp2 = max([tmp,dp[i][j-1]])
                dp[i][j]=min([tmp2,dp[i][j]])
            if j<cols-1:
                tmp=abs(heights[i][j]-heights[i][j+1])
                tmp2 = max([tmp,dp[i][j+1]])
                dp[i][j]=min([tmp2,dp[i][j]])
        def updateNei(i,j):
            if i>=1:
                tmp=dp[i-1][j]
                update(i-1,j)
                if tmp>dp[i-1][j]:
                    updateNei(i-1,j)
            if i<rows-1:
                tmp=dp[i+1][j]
                update(i+1,j)
                if tmp>dp[i+1][j]:
                    updateNei(i+1,j)
            if j>=1:
                tmp = dp[i][j-1]
                update(i,j-1)
                if tmp>dp[i][j-1]:
                    updateNei(i,j-1)
            if j<cols-1:
                tmp=dp[i][j+1]
                update(i,j+1)
                if tmp>dp[i][j+1]:
                    updateNei(i,j+1)
        for i in range(rows):
            for j in range(cols):
                tmp = dp[i][j]
                update(i,j)
                if tmp> dp[i][j]:
                    updateNei(i,j)
        return dp[rows-1][cols-1]

sol = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(sol.minimumEffortPath(heights))
