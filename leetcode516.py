# 516. 最长回文子序列
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==s[-j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        return dp[n][n]

sol = Solution()
s = "cbbd"
print(sol.longestPalindromeSubseq(s))
