# 688. 骑士在棋盘上的概率
# 在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。

# 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/knight-probability-in-chessboard
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#超时
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        ans = 0
        diff = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        def dfs(step,x,y):
            if step==k:
                return
            nonlocal ans
            for tx,ty in diff:
                nx=x+tx
                ny=y+ty
                if 0<=nx<n and 0<=ny<n:
                    dfs(step+1,nx,ny)
                else:
                    ans+=1/(8**(step+1))
        dfs(0,row,column)
        return 1-ans


class Solution2:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        diff = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        dp = [[[0]*n for _ in range(n)] for _ in range(k+1)]
        for step in range(k+1):
            for i in range(n):
                for j in range(n):
                    if step==0:
                        dp[step][i][j]=1
                    else:
                        for tx,ty in diff:
                            nx=i+tx
                            ny=j+ty
                            if 0<=nx<n and 0<=ny<n:
                                dp[step][i][j]+=dp[step-1][nx][ny]/8
        return dp[k][row][column]


sol = Solution2()
n = 3
k = 2
row = 0
column = 0
print(sol.knightProbability(n,k,row,column))
            
