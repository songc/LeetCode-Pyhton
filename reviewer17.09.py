# 面试题 17.09. 第 k 个数
# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/get-kth-magic-number-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        if k ==1:
            return 1
        dp = [0,0,0]
        ans = [1]
        while len(ans)<k:
            dp3 = 3*ans[dp[0]]
            dp5 = 5*ans[dp[1]]
            dp7 = 7*ans[dp[2]]
            target = min(dp3,dp5,dp7)
            if target==dp3:
                dp[0]+=1
            if target==dp5:
                dp[1]+=1
            if target==dp7:
                dp[2]+=1
            ans.append(target)
        return ans[-1]


sol = Solution()
print(sol.getKthMagicNumber(10))