# 338. 比特位计数
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1,num+1):
            ans.append(ans[i>>1]+(i&1))
        return ans

class Solution2:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1,num+1):
            ans.append(ans[i&(i-1)]+1)
        return ans

sol = Solution2()

print(sol.countBits(10))
