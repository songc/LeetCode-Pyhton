# 1049. 最后一块石头的重量 II
# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/last-stone-weight-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n,m = len(stones),total//2
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(n):
            for j in range(m+1):
                if j<stones[i]:
                    dp[i+1][j]=dp[i][j]
                else:
                    dp[i+1][j]=dp[i][j] or dp[i][j-stones[i]]
        ans = None
        for j in range(m,-1,-1):
            if dp[n][j]:
                ans = total-2*j
                break
        return ans
        

sol = Solution()
stones = [31,26,33,21,40]
print(sol.lastStoneWeightII(stones))