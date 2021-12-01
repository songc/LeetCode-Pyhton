# 1446. 连续字符
# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

# 请你返回字符串的能量。


class Solution:
    def maxPower(self, s: str) -> int:
        left=0
        right=0
        n=len(s)
        res= 0
        while right<n:
            if s[right]==s[left]:
                right+=1
            else:
                res=max(res,right-left)
                left=right
        res=max(res,right-left)
        return res

sol = Solution()
print(sol.maxPower("leetcode"))