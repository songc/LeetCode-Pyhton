# 313. 超级丑数
# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import heapq
import collections


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = []
        head = [1]
        visited = set()
        for i in range(n):
            x = heapq.heappop(head)
            dp.append(x)
            for p in primes:
                px = x*p
                if px not in visited:
                    heapq.heappush(head, px)
                visited.add(px)
        return dp[-1]


class Solution2:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        m = len(primes)
        pointers = [0] * m

        for i in range(1, n):
            min_num = min((dp[pointers[j]]*primes[j] for j in range(m)))
            dp[i] = min_num
            for j in range(m):
                if dp[pointers[j]]*primes[j] == min_num:
                    pointers[j] += 1

        return dp[-1]


class Solution3:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        m = len(primes)
        pointers = [(p, 0, i) for i, p in enumerate(primes)]
        heapq.heapify(pointers)

        for i in range(1, n):
            dp[i] = pointers[0][0]
            while pointers and pointers[0][0] == dp[i]:
                _, ind, pindx = heapq.heappop(pointers)
                heapq.heappush(
                    pointers, (primes[pindx]*dp[ind+1], ind+1, pindx))

        return dp[-1]


sol = Solution3()
n = 12
primes = [2, 7, 13, 19]
print(sol.nthSuperUglyNumber(n, primes))
