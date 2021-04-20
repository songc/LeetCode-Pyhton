# 28. 实现 strStr()
# 实现 strStr() 函数。

# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

#  

# 说明：

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-strstr
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        l1,l2 = len(haystack),len(needle)
        if l1==l2:
            return 0 if haystack==needle else -1
        for i in range(l1-l2+1):
            if haystack[i]==needle[0] and haystack[i+l2-1]==needle[-1]:
                if haystack[i:i+l2] == needle:
                    return i
        return -1

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        i=j=0
        m,n = len(haystack), len(needle)
        nextJ = self.kmp(needle)
        j=0
        for i in range(0,m):
            while j>0 and haystack[i]!=needle[j]:
                j=nextJ[j-1]
            if haystack[i]==needle[j]:
                j+=1
            if j==n:
                return i-n+1
        return -1
    def kmp(self, s: str) -> list:
        ans = [0]*len(s)
        for i in range(1,len(s)):
            j = ans[i-1]
            while j>0 & s[i]!=s[j]:
                j=ans[j-1]
            if s[i]==s[j]:
                j+=1
            ans[i]=j
        return ans

sol = Solution2()
haystack = "abc"
needle = "c"
print(sol.strStr(haystack,needle))