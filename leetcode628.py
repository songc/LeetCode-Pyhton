# 628. 三个数的最大乘积
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
import heapq
class Solution:
    def maximumProduct(self, nums: list) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])