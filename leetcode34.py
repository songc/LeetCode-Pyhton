# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 进阶：

# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if len(nums)<1:
            return [-1,-1]
        left = self.searchLeft(nums,target)
        if left==-1:
            return [-1,-1]
        else:
            return [left,self.searchRight(nums,target,left)]
    def searchLeft(self, nums: list, target: int,lo=0, hi=None) -> int:
        if hi==None:
            hi=len(nums)
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid]==target:
                hi=mid
            elif nums[mid]>target:
                hi=mid
            elif nums[mid]<target:
                lo=mid+1
        if lo<len(nums) and nums[lo]==target:
            return lo
        else:
            return -1
    
    def searchRight(self, nums: list, target: int, lo = 0, hi = None) -> int:
        if hi==None:
            hi = len(nums)
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid]==target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid
            elif nums[mid]<target:
                lo=mid+1
        if nums[lo-1]==target:
            return lo-1
        else:
            return -1

sol=Solution()
nums = [2,2]
target = 8
print(sol.searchRange(nums,target))



