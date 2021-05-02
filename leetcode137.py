# 137. 只出现一次的数字 II
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

from typing import List
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=3
        return nums[-1]

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for key in counter:
            if counter[key]==1:
                return key

sol = Solution2()
nums = [0,1,0,1,0,1,99]
print(sol.singleNumber(nums))
                