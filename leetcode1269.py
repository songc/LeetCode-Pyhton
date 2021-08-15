# 1269. 停在原地的方案数
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

# 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

# 由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9+7
        maxCols = min(arrLen,steps)
        dp = [[0] * (steps+1) for _ in range(maxCols)]
        dp[0][0] = 1
        for j in range(1, steps+1):
            for i in range(maxCols):
                s = 0
                if i-1 >= 0:
                    s += dp[i-1][j-1]
                if i+1 < maxCols:
                    s += dp[i+1][j-1]
                dp[i][j] = (s+dp[i][j-1]) %mod
        return dp[0][-1]


sol = Solution()
steps = 4
arrLen = 3
print(sol.numWays(steps, arrLen))
