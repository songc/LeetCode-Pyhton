# 283. 移动零

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
            nums.append(0)

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0
        n = len(nums)
        while right<n:
            if nums[right]==0:
                right+=1
                continue
            while left<right and nums[left]!=0:
                left+=1
            if left<right:
                nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right+=1

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0
        n = len(nums)
        while right<n:
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1

class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0
        n = len(nums)
        while right<n:
            if nums[right]!=0:
                nums[left]=nums[right]
                left+=1
            right+=1
        while left<n:
            nums[left]=0
            left+=1
    
        
        
        
        