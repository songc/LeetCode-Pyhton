class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        ri, rj, maxL = 0,0,1
        for k in range(n):
            for i in range(n):
                j=i+k
                if j>=n:
                    break
                if i==j:
                    dp[i][j]=1
                else:
                    if s[i]==s[j]: 
                        if i+1==j:
                            dp[i][j]=j-i+1
                        elif dp[i+1][j-1]>0:
                            dp[i][j]=j-i+1
                    if dp[i][j]>maxL:
                        maxL=dp[i][j]
                        ri=i
                        rj=j
        return s[ri:rj+1]

s= Solution()
chars = "cbbd"
print(s.longestPalindrome(chars))

         
