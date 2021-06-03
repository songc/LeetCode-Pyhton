# 477. 汉明距离总和
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

# 计算一个数组中，任意两个数之间汉明距离的总和。

from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans