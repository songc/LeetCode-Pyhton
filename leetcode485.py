# 485. 最大连续1的个数
# 给定一个二进制数组， 计算其中最大连续 1 的个数。
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        tmp = 0
        for i in nums:
            if i==0:
                ans = max(tmp,ans)
                tmp = 0
            else:
                tmp +=1
        ans = max(tmp,ans)
        return ans