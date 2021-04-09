# 647. 回文子串
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp=[[0]*(n) for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
        for k in range(1,n):
            for i in range(n):
                j = i+k
                if j>=n:
                    break
                if s[i] == s[j]:
                    if j-i==1 or dp[i+1][j-1]==1:
                        dp[i][j]=1
        return sum([sum(i) for i in dp])

sol = Solution()
s="aaaaa"
print(sol.countSubstrings(s))
        