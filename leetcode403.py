# 403. 青蛙过河
# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

# 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

# 开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/frog-jump
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp0 = [False]*n
        dp1 = [set() for _ in range(n)]
        dp2 = [0]*n
        dp0[0]=True
        dp1[0].add(1)
        dp2[0]=1
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if not dp0[j]:
                    continue
                if dp2[j]<stones[i]:
                    continue
                step=stones[i]-stones[j]
                tmpset = set([step-1,step,step+1])
                if tmpset.intersection(dp1[j]):
                    dp0[i]=True
                    dp1[i].add(step)
                    nextStones = stones[i]+step+1
                    if nextStones>dp2[i]:
                        dp2[i]=nextStones
        return dp0[-1]


class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp0 = [False]*n
        dp1 = [set() for _ in range(n)]
        dp2 = [0]*n
        dp0[0]=True
        dp1[0].add(1)
        dp2[0]=1
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if not dp0[j]:
                    continue
                if dp2[j]<stones[i]:
                    continue
                step=stones[i]-stones[j]
                if step in dp1[j]:
                    dp0[i]=True
                    dp1[i].add(step)
                    dp1[i].add(step+1)
                    if step-1:
                        dp1[i].add(step-1)
                    nextStones = stones[i]+step+1
                    if nextStones>dp2[i]:
                        dp2[i]=nextStones
        return dp0[-1]
sol = Solution()
stones = [0,2]
print(sol.canCross(stones))
