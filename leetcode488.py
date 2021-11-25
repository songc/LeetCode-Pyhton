# 488. 祖玛游戏
# 你正在参与祖玛游戏的一个变种。

# 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。

# 你的目标是 清空 桌面上所有的球。每一回合：

# 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
# 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
# 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
# 如果桌面上所有球都被移除，则认为你赢得本场游戏。
# 重复这个过程，直到你赢了游戏或者手中没有更多的球。
# 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zuma-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from functools import lru_cache
import re
from collections import deque

# 超时
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        boardList = tuple(board)
        handList =tuple(sorted(hand))

        @lru_cache()
        def backtrack(boardList, handTuple, step):
            minStep = float('inf')
            if len(boardList) == 0:
                return step
            if len(handTuple)==0:
                return minStep
            n = len(boardList)
            for i in range(n):
                for key in handTuple:
                    tmp = list(boardList)
                    tmp.insert(i, key)
                    newHand = list(handTuple)
                    newHand.remove(key)
                    minStep = min(minStep, backtrack(tuple(self.removeSame(tmp)), tuple(newHand), step+1))
            return minStep
        res = backtrack(tuple(boardList), handList, 0)
        return -1 if res == float("inf") else res

    def removeSame(self, content: list):
        target = None
        count = 0
        for i in range(len(content)):
            if content[i] == target:
                count += 1
            else:
                if count >= 3:
                    return self.removeSame(content[:i-count]+content[i:])
                target = content[i]
                count = 1
        if count >= 3:
            return content[:i-count+1]
        return content

# 广度优先，Astart+ 剪枝
class Solution2:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            n=1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s
        hand = "".join(sorted(hand))

        queue = deque([(board,hand,0)])
        visited = set([(board,hand)])
        while queue:
            newBoard,newHand,step = queue.popleft()
            for i in range(len(newBoard)+1):
                for j in range(len(newHand)):
                    if j>0 and newHand[j]==newHand[j-1]:
                        continue
                    if i>0 and newHand[j]==newBoard[i-1]:
                        continue
                    flag = False
                    if 0<i<len(newBoard) and newBoard[i]==newBoard[i-1]:
                        flag = True
                    if i<len(newBoard) and newBoard[i]==newHand[j]:
                        flag = True
                    if flag:
                        nextBoard = clean(newBoard[:i]+newHand[j]+newBoard[i:])
                        nextHand = newHand[:j]+newHand[j+1:]
                        if not nextBoard:
                            return step+1
                        if (nextBoard,nextHand) not in visited:
                            visited.add((nextBoard,nextHand))
                            queue.append((nextBoard,nextHand,step+1))
        return -1


# 比较慢
class Solution3:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            n=1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s
        hand = "".join(sorted(hand))

        # 有step  无法记忆化搜索
        def backtrace(newBoard,newHand,step):
            if not newBoard:
                return step
            if not newHand:
                return 6
            res = 6
            for i in range(len(newBoard)+1):
                for j in range(len(newHand)):
                    if j>0 and newHand[j]==newHand[j-1]:
                        continue
                    if i>0 and newHand[j]==newBoard[i-1]:
                        continue
                    flag = False
                    if 0<i<len(newBoard) and newBoard[i]==newBoard[i-1]:
                        flag = True
                    if i<len(newBoard) and newBoard[i]==newHand[j]:
                        flag = True
                    if flag:
                        nextBoard = clean(newBoard[:i]+newHand[j]+newBoard[i:])
                        nextHand = newHand[:j]+newHand[j+1:]
                        res= min(res,backtrace(nextBoard,nextHand,step+1))
            return res
        ans = backtrace(board,hand,0)
        return ans if ans<6 else -1

# 记忆化搜索
class Solution4:
    def findMinStep(self, board: str, hand: str) -> int:
        @lru_cache(None)
        def clean(s):
            n=1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s
        hand = "".join(sorted(hand))

        @lru_cache(None)        
        def backtrace(newBoard,newHand):
            if not newBoard:
                return 0
            res = 6
            for i in range(len(newBoard)+1):
                for j in range(len(newHand)):
                    if j>0 and newHand[j]==newHand[j-1]:
                        continue
                    if i>0 and newHand[j]==newBoard[i-1]:
                        continue
                    flag = False
                    if 0<i<len(newBoard) and newBoard[i]==newBoard[i-1]:
                        flag = True
                    if i<len(newBoard) and newBoard[i]==newHand[j]:
                        flag = True
                    if flag:
                        nextBoard = clean(newBoard[:i]+newHand[j]+newBoard[i:])
                        nextHand = newHand[:j]+newHand[j+1:]
                        res= min(res,backtrace(nextBoard,nextHand)+1)
            return res
        ans = backtrace(board,hand)
        return ans if ans<6 else -1

sol = Solution4()
board =  "RRYGGYYRRYGGYYRR" 
hand = "GGBBB"
print(sol.findMinStep(board, hand))
