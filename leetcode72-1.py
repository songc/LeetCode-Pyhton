from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache()
        def dp(i,j):
            if i==-1 and j==-1:
                return 0
            if i==-1:
                return j+1
            if j==-1:
                return i+1
            if word1[i]==word2[j]:
                return dp(i-1,j-1)
            else:
                return min(dp(i-1,j-1),dp(i-1,j),dp(i,j-1))+1
        return dp(len(word1)-1,len(word2)-1)

sol = Solution()
word1 = "intention"
word2 = "execution"
print(sol.minDistance(word1,word2))