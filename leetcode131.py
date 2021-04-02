# 131. 分割回文串
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回 s 所有可能的分割方案。
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isRev(chars):
            left = 0
            right = len(chars)-1
            if right == 0:
                return True
            while left<right:
                if chars[left] != chars[right]:
                    return False
                left+=1
                right-=1
            return True
        ans = []
        if len(s)==1:
            ans.append([s])
            return ans
        
        def backtract(cnt, strings, ind):
            if ind>=len(strings):
                ans.append(list(cnt))
                return
            for i in range(1,len(strings)+1):
                if ind+i<=len(strings):
                    tmp = strings[ind:ind+i]
                    if isRev(tmp):
                        cnt.append(tmp)
                        backtract(cnt,strings,ind+i)
                        cnt.pop()
        backtract([],s,0)
        return ans

sol = Solution()
s = "aa"
print(sol.partition(s))
