# 482. 密钥格式化
# 有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。

# 给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

# 给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/license-key-formatting
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        tmp = s.replace("-","").upper()
        n = len(tmp)
        first = n%k
        res = []
        if first:
            res.append(tmp[0:first])
        for i in range(first,n-k+1,k):
            res.append(tmp[i:i+k])
        return "-".join(res)


class Solution2:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        cnt=0
        for char in s[::-1]:
            if char != "-":
                res.append(char.upper())
                cnt+=1
                if cnt%k==0:
                    res.append("-")
        if res and res[-1]=="-":
            res.pop()
        return "".join(res[::-1])



sol = Solution2()
S = "5F3Z-2e-9-w"
K = 4
print(sol.licenseKeyFormatting(S,K))