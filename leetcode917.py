# 917. 仅仅反转字母
# 给你一个字符串 s ，根据下述规则反转字符串：

# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left,right = 0,len(ans)-1
        while left<right:
            while left<right and not ans[left].isalpha():
                left+=1
            while left<right and not ans[right].isalpha():
                right-=1
            ans[left],ans[right]=ans[right],ans[left]
            left+=1
            right-=1
        return "".join(ans)

sol = Solution()
s = "a-bC-dEf-ghIj"
print(sol.reverseOnlyLetters(s))
