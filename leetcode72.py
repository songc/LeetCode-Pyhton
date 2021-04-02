# 72. 编辑距离
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/edit-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [ [0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    dp[i][j]=0
                elif i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    if word1[i-1]==word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]

sol = Solution()
word1 = "intention"
word2 = "execution"
print(sol.minDistance(word1,word2))
            