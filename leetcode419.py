# 419. 甲板上的战舰
# 给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。

# 战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/battleships-in-a-board
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 并查集
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board),len(board[0])
        parent = [i for i in range(m*n)]
        def findRoot(x):
            if parent[x]!=x:
                parent[x]=findRoot(parent[x])
            return parent[x]
        def union(x,y):
            rootX = findRoot(x)
            rootY = findRoot(y)
            parent[rootX]=rootY
        for i in range(m):
            for j in range(n):
                if board[i][j]==".":
                    parent[i*n+j]=-1
                    continue
                if i>0 and board[i-1][j]=="X":
                    parent[i*n+j]=findRoot(i*n-n+j)
                if j>0 and board[i][j-1]=="X":
                    parent[i*n+j]=findRoot(i*n-1+j)
        vset = set()
        for i in range(m*n):
            r = findRoot(i)
            if r != -1:
                vset.add(r)
        return len(vset)


# 单次扫描
class Solution2:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board),len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]==".":
                    continue
                if i>0 and board[i-1][j]=="X":
                    continue
                if j>0 and board[i][j-1]=="X":
                    continue
                res+=1
        return res

sol = Solution2()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(sol.countBattleships(board))
