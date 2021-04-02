# 567. 字符串的排列
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetCounter = collections.Counter(s1)
        targetN=len(s1)
        left,right=0,0
        n = len(s2)
        tmpCounter = collections.Counter()
        while right<n:
            if s2[right] not in targetCounter:
                right+=1
                left = right
                tmpCounter=collections.Counter()
                continue
            tmpCounter[s2[right]]+=1
            while tmpCounter[s2[right]]>targetCounter[s2[right]]:
                tmpCounter[s2[left]]-=1
                left+=1
            right+=1
            if right-left==targetN:
                return True
        return False

sol = Solution()
s1 = "ab" 
s2 = "eidboaoo"
print(sol.checkInclusion(s1,s2))
            

