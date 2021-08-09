# 1137. 第 N 个泰波那契数
# 泰波那契序列 Tn 定义如下： 

# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        if n<3:
            return dp[n]
        tmp = 2
        for i in range(3,n+1):
            dp.append(tmp)
            tmp=tmp*2-dp[i-3]
        return dp[-1]

sol = Solution()
print(sol.tribonacci(25))
            