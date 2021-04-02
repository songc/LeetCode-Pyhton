from typing import List
import collections

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = self.subarraysWithMaxKDist(A,K)-self.subarraysWithMaxKDist(A,K-1)
        return ans
    
    def subarraysWithMaxKDist(self, A: List[int], K: int) -> int:
        counter = collections.Counter()
        dist = 0
        left=right=0
        res=0
        while right<len(A):
            if counter[A[right]]==0:
                dist+=1
            counter[A[right]]+=1
            while dist>K:
                counter[A[left]]-=1
                if counter[A[left]]==0:
                    dist-=1
                left+=1
            res += right-left+1
            right+=1
        return res

sol = Solution()
A=[2,2,1,2,2,2,1,1]
K=2
print(sol.subarraysWithKDistinct(A,K))
            
