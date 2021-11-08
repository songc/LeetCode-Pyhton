# 268. 丢失的数字
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2-sum(nums)

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res^=nums[i]
            res^=i
        return res

sol = Solution2()
nums = [1,0,3]
print(sol.missingNumber(nums)) 