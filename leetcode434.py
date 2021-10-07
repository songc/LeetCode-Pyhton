# 434. 字符串中的单词数
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

# 请注意，你可以假定字符串里不包括任何不可打印的字符。

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

class Solution2:
    def countSegments(self, s: str) -> int:
        s+=" "
        n = len(s)
        res=0
        for i in range(1,n):
            if s[i]==" " and s[i-1] != " ":
                res+=1
        return res
sol = Solution()
s=", , , ,        a, eaefa"
print(sol.countSegments(s))