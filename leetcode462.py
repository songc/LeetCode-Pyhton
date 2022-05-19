# 462. 最少移动次数使数组元素相等 II
# 给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。

# 在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(abs(nums[i]-nums[len(nums)//2]) for i in range(len(nums)))