# 926. 将字符串翻转到单调递增
# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。

# 给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。

# 返回使 s 单调递增的最小翻转次数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/flip-string-to-monotone-increasing
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from tkinter import N


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num1 = 0
        num0 = 0
        for c in s:
            if c=='0' and num1>0:
                num0+=1
                if num0>=num1:
                    ans+=num1
                    num1=num0=0
            elif c=='1':
                num1+=1
                if num1==1:
                    num0=0
        ans+=num0
        return ans

# 动态规划
class Solution2:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp=0
        num1 = 0
        for c in s:
            if c=='0':
                dp = min(dp+1,num1)
            elif c=='1':
                num1+=1
        return dp

sol = Solution2()
s = "00011000"
print(sol.minFlipsMonoIncr(s))
            
