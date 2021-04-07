# 81. 搜索旋转排序数组 II
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # def searchIn(nums,target,left=0,right=None):
        #     if right==None or right>len(nums):
        #         right = len(nums)
        #     while left<right:
        #         mid = (left+right)//2
        #         if nums[mid]==target:
        #             return True
        #         elif target>nums[mid]:
        #             if nums[mid]>nums[left]:
        #                 left=mid+1
        #             elif nums[mid]==nums[left]:
        #                 return searchIn(nums,target,left+1,mid) or searchIn(nums,target,mid+1,right)
        #             else:
        #                 right=mid
        #         elif target<nums[mid]:
        #             if nums[left]>nums[mid]:
        #                 right=mid
        #             elif nums[mid]==nums[left]:
        #                 return searchIn(nums,target,left,mid) or searchIn(nums,target,mid+1,right)
        #             else:
        #                 left=mid+1
        #     return False
        # return searchIn(nums,target)
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            if  nums[left]==nums[mid]:
                left+=1
            elif nums[left] < nums[mid]:
                if target<nums[mid] and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1
            else: 
                if target>nums[mid] and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return False
        

nums = [2,5,6,0,0,1,2]

target = 5
sol = Solution()
print(sol.search(nums,target))