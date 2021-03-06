# 877. 石子游戏
# 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

# 游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

# 亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

# 假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/stone-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=piles[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0


sol = Solution()
piles = [5,3,4,5]
print(sol.stoneGame(piles))