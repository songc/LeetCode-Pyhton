# 1208. 尽可能使字符串相等
# 给你两个长度相同的字符串，s 和 t。

# 将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

# 用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

# 如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

# 如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/get-equal-substrings-within-budget
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffList = []
        for ss,tt in zip(s,t):
            diffList.append(abs(ord(ss)-ord(tt)))
        begin,end = 0,0
        tmp =0
        for i in range(len(diffList)):
            tmp = tmp+diffList[i]
            end+=1
            if tmp>maxCost:
                tmp-=diffList[begin]
                begin+=1
        return end-begin

sol = Solution()
s = "abcd"
t = "acde"
cost = 0
print(sol.equalSubstring(s,t,cost))
                
        