# 1763. 最长的美好子字符串
# 当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。比方说，"abABB" 是美好字符串，因为 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。

# 给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-nice-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ""
        n = len(s)
        for i in range(n):
            for j in range(i,n+1):
                if j-i<=len(res):
                    continue
                tmp = set(s[i:j])
                flag=True
                for k in tmp:
                    if ord(k)<91 and chr(ord(k)+32) not in tmp:
                        flag=False
                        break
                    if ord(k)>=91 and chr(ord(k)-32) not in tmp:
                        flag=False
                        break
                if flag:
                    res=s[i:j]
        return res

sol = Solution()
s="YazaAay"
print(sol.longestNiceSubstring(s))