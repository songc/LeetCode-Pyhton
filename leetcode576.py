# 576. 出界的路径数
# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

# 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/out-of-boundary-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = []
        mod = 10**9+7
        chage = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range (m):
            tmp =[]
            for j in range(n):
                tmp.append([0]*(maxMove+1))
            dp.append(tmp)
        for z in range(1,maxMove+1):
            for i in range(m):
                for j in range(n):
                    tmp = 0
                    for cx,cy in chage:
                        x,y = i+cx,j+cy
                        if 0<=x<m and 0<=y<n:
                            tmp +=dp[x][y][z-1]
                        else:
                            tmp += 1
                    dp[i][j][z]=tmp%mod
        return dp[startRow][startColumn][-1]

sol = Solution()
m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
print(sol.findPaths(m,n,maxMove,startRow,startColumn))
