# 794. 有效的井字游戏
# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。

# 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。

# 以下是井字游戏的规则：

# 玩家轮流将字符放入空位（' '）中。
# 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
# 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
# 当所有位置非空时，也算为游戏结束。
# 如果游戏结束，玩家不允许再放置字符。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-tic-tac-toe-state
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xnum,onum=0,0
        xlist,olist = 0,0
        for i in range(3):
            for j in range(3):
                if board[i][j]=="X":
                    xnum+=1
                if board[i][j]=="O":
                    onum+=1
            if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=' ':
                if board[i][0]=="X":
                    xlist+=1
                else:
                    olist+=1
            if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=' ':
                if board[0][i]=="X":
                    xlist+=1
                else:
                    olist+=1
        if onum>xnum:
            return False
        if xnum>onum+1:
            return False
        if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=' ':
            if board[0][0]=="X":
                xlist+=1
            else:
                olist+=1
        if board[2][0]==board[1][1]==board[0][2] and board[2][0]!=' ':
            if board[2][0]=="X":
                xlist+=1
            else:
                olist+=1
        if xlist>0 and olist>0:
            return False
        if xlist>0 and onum==xnum:
            return False
        if olist>0 and xnum>onum:
            return False
        return True

sol = Solution()
board = ["XO ","XO ","XO "]
print(sol.validTicTacToe(board))
        

        
