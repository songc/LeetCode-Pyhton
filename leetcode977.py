# 977. 有序数组的平方
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left = 0
        n = len(nums)
        right = n-1
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                res.append(nums[left]**2)
                left+=1
            else:
                res.append(nums[right]**2)
                right-=1
        res.reverse()
        return res

