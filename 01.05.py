# 面试题 01.05. 一次编辑
# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。


from distutils.command.build_scripts import first_line_re


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i+1][0]=i+1
        for i in range(n):
            dp[0][i+1]=i+1
        for i in range(m):
            for j in range(n):
                if first[i]==second[j]:
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i][j],dp[i+1][j])+1
        return dp[m][n]<=1

sol = Solution()
first = "pales"
second = "pal"
print(sol.oneEditAway(first,second))
