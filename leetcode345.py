# 345. 反转字符串中的元音字母
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        allSet = set(['a','e','i','o','u',"A",'E','I','O','U'])
        s = [c for c in s]
        left,right = 0, n-1
        while left<right:
            while left<right and s[left] not in allSet:
                left+=1
            while left<right and s[right] not in allSet:
                right-=1
            if s[left] in allSet and s[right] in allSet:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)

sol = Solution()
s = "hello"
print(sol.reverseVowels(s))
