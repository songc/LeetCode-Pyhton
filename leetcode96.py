from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache()
        def f(k):
            if k ==1:
                return 1
            if k==2:
                return 2
            if k==3:
                return 5
            ans = 0
            ans+=2*f(k-1)
            for i in range(1,k-1):
                ans+=f(i)*f(k-1-i)
            return ans
        return f(n)

sol=Solution()
print(sol.numTrees(4))
