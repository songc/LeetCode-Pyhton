# 215. 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k>n//2:
            return self.findKthMin(nums,n-k)
        for i in range(k):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums[k-1]

    def findKthMin(self,nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(k):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums[k-1]