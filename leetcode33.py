# 33. 搜索旋转排序数组
# 升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。

# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def search(self, nums: list, target: int) -> int:
        if target>nums[0]:
            return self.searchLeft(nums,target)
        elif target==nums[0]:
            return 0
        elif target<nums[0]:
            return self.searchRight(nums,target)

    def searchLeft(self,nums:list,target: int) -> int:
        lo = 0
        hight = len(nums)-1
        while lo<=hight:
            mid = (lo+hight)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                if nums[mid]>=nums[0]:
                    lo=mid+1
                else:
                    hight = mid-1
            elif nums[mid]>target:
                hight=mid-1
        return -1
    def searchRight(self, nums:list, target:int):
        lo=0
        hight=len(nums)-1
        while lo<=hight:
            mid = (lo+hight)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                lo = mid+1
            elif nums[mid]>target:
                if nums[mid]>=nums[0]:
                    lo=mid+1
                else:
                    hight=mid-1
        return -1

sol = Solution()
nums = [1,2]
target = 3
print(sol.search(nums,target))
