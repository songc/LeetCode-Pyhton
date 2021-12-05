# 372. 超级次方
# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD =1337
        ans = 1
        for e in reversed(b):
            ans = ans*pow(a,e,MOD)%MOD
            a = pow(a,10,MOD)
        return ans

sol = Solution()
a = 2
b = [1,0]
print(sol.superPow(a,b))