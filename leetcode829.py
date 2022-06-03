# 829. 连续整数求和
# 给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 

from collections import deque

# 超时
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        q = deque()
        q.append(0)
        for i in range(1,n+1):
            q.append(q[-1]+i)
            target = q[-1]-n
            while q[0]<target:
                q.popleft()
            if q[0]==target:
                ans+=1
        return ans


class Solution2:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isContrunct(n,k):
            if k%2==1:
                return n%k==0
            return n%k and 2*n%k==0
        ans = 0
        k = 1
        while k*(k+1)<=n*2:
            if isContrunct(n,k):
                ans+=1
            k+=1
        return ans


sol = Solution2()
print(sol.consecutiveNumbersSum(15))
