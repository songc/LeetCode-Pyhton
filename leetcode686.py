# 686. 重复叠加字符串匹配
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/repeated-string-match
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(b)==0:
            return 0
        begin = a.find(b)
        if begin!=-1:
            return 1
        begin = (a+a).find(b)
        if begin!=-1:
            return 2
        begin = b.find(a)
        if begin==-1:
            return -1
        res=0
        if begin==0:
            res=0
        elif  a.endswith(b[:begin]):
            res=1
        else:
            return -1
        n = len(a)
        for i in range(begin,len(b)):
            if a[(i-begin)%n]!=b[i]:
                return -1
        div,mod = divmod(len(b)-begin,n)
        return res+div+1 if mod else res+div

sol = Solution()
a = "abcd"
b = "cdabcdab"
print(sol.repeatedStringMatch(a,b))


