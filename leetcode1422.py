# 1422. 分割字符串的最大得分
# 给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。

# 「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-score-after-splitting-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxScore(self, s: str) -> int:
        num1 = s.count("1")
        ans = num1+1 if s[0]=='0' else max(0,num1-1)
        tmp = ans
        for i in range(1,len(s)-1):
            if s[i]=="0":
                tmp+=1
            else:
                tmp-=1
            ans = max(tmp,ans)
        return ans

sol = Solution()
s = "011101"
print(sol.maxScore(s))
