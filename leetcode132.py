# 132. 分割回文串 II
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

# 返回符合要求的 最少分割次数 。

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for k in range(n):
            for i in range(n):
                j = i+k
                if j>=n:
                    break
                if i==j:
                    dp[i][j]=True
                elif j==i+1 and s[i]==s[j]:
                    dp[i][j]=True
                elif s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
        dp2 = [float('inf')]*n
        for i in range(n):
            if dp[0][i]:
                dp2[i]=0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        dp2[i] = min(dp2[i],dp2[j]+1)
        return dp2[-1]

sol = Solution()
s = "ab"
print(sol.minCut(s))
            



