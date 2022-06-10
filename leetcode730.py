# 730. 统计不同回文子序列
# 给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。

# 通过从 s 中删除 0 个或多个字符来获得子序列。

# 如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。

# 如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。

# 注意：
# 结果可能很大，你需要对 109 + 7 取模 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/count-different-palindromic-subsequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        mod = 10**9+7
        dp=[[[0]*n for _ in range(n)] for _ in range(4)]
        for i,c in enumerate(s):
            dp[ord(c)-ord('a')][i][i]=1
        for sz in range(2,n+1):
            for j in range(sz-1,n):
                i=j-sz+1
                for k,c in enumerate('abcd'):
                    if s[i]==c and s[j]==c:
                        dp[k][i][j]= (2+sum(d[i+1][j-1] for d in dp))%mod
                    elif s[i]==c:
                        dp[k][i][j]=dp[k][i][j-1]
                    elif s[j]==c:
                        dp[k][i][j]=dp[k][i+1][j]
                    else:
                        dp[k][i][j]=dp[k][i+1][j-1]
        return sum(d[0][n-1] for d in dp)%mod