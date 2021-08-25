# 541. 反转字符串 II
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-string-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        n = len(s)
        tmp = []
        flag = True
        for i in range(n):
            tmp.append(s[i])
            if len(tmp)==k or i==n-1:
                if flag:
                    tmp.reverse()
                    res.extend(tmp)
                    flag = False
                else:
                    res.extend(tmp)
                    flag = True
                tmp = []
        return "".join(res)

sol = Solution()
s = "abcdefg"
k = 2
print(sol.reverseStr(s, k))
