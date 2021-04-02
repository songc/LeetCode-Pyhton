from typing import List
import collections

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ans = 0
        queue = collections.deque()
        n = len(A)
        for i in range(n):
            if queue and i >= queue[0]+K:
                queue.popleft()
            if len(queue)%2==A[i]:
                if i+K>n:
                    return -1
                queue.append(i)
                ans+=1
        return ans

sol = Solution()
A = [0,0,0,1,0,1,1,0]
K = 3
print(sol.minKBitFlips(A,K))