import collections
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque=collections.deque()
        n = len(nums)
        ans = []
        for i in range(k):
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
        for i in range(k,n):
            ans.append(deque[0])
            while deque and deque[-1]<nums[i]:
                deque.pop()
            deque.append(nums[i])
            if deque[0]==nums[i-k]:
                deque.popleft()
        ans.append(deque[0])
        return ans

                
            
