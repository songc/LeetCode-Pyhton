# 664. 奇怪的打印机
# 有台奇怪的打印机有以下两个特殊要求：

# 打印机每次只能打印由 同一个字符 组成的序列。
# 每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
# 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/strange-printer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=min((dp[i][k]+dp[k+1][j] for k in range(i,j)))
        return dp[0][n-1]

sol = Solution()
s = "aba"
print(sol.strangePrinter(s))
            
