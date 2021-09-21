# 58. 最后一个单词的长度
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        ind = s.rfind(' ')
        return len(s)-ind-1

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n-1,-1,-1):
            if s[i]!=" ":
                res+=1
            else:
                if res:
                    return res
        return res
sol = Solution2()
s =  "   fly me   to   the moon  "
print(sol.lengthOfLastWord(s))
