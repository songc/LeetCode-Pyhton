# 152. 乘积最大子数组
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans=nums[0]
        for i in range(n):
            tmp = nums[i]
            if tmp > ans:
                ans = tmp
            for j in range(i+1,n):
                tmp = tmp*nums[j]
                if tmp > ans:
                    ans = tmp
        return ans