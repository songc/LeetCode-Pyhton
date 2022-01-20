# 2029. 石子游戏 IX
# Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 stones ，其中 stones[i] 是第 i 个石子的价值。

# Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 stones 中移除任一石子。

# 如果玩家移除石子后，导致 所有已移除石子 的价值 总和 可以被 3 整除，那么该玩家就 输掉游戏 。
# 如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。
# 假设两位玩家均采用 最佳 决策。如果 Alice 获胜，返回 true ；如果 Bob 获胜，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/stone-game-ix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 不考虑0的情况时所取的序列有两种情况112121212....和221212121....0可以插入在任意非首位的位置

# 当s[0]为偶数时，若1或2个数为零，要么石头能取完，要么111Alice会拿到3的倍数也会输；

# 若均不为零时，Alice取少的一个则必赢，相等时取任一个均能赢

# 当s[0]为奇数时，次序能颠倒，故当1和2个数相差大于2时，取多的一个则在颠倒次序后alice必赢，否则就输

# 妈呀好绕，理了半天

from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        numCount = [0,0,0]
        for i in stones:
            numCount[i%3]+=1
        if numCount[0]%2==0:
            return numCount[1]>0 and numCount[2]>0
        return abs(numCount[1]-numCount[2])>2