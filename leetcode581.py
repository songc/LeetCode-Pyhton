# 581. 最短无序连续子数组
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 请你找出符合题意的 最短 子数组，并输出它的长度。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        newNums = sorted(nums)
        left =0
        right = len(nums)-1
        while left<right:
            if nums[left]!=newNums[left]:
                break
            left+=1
        while left<right:
            if nums[right]!=newNums[right]:
                break
            right-=1
        if right-left:
            return right-left+1
        return right-left

class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = None
        right = None
        max_l = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>=max_l:
                max_l=nums[i]
            else:
                right = i
        if not right:
            return 0
        min_l = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=min_l:
                min_l=nums[i]
            else:
                left=i
        return right-left+1

nums = [2,6,4,8,10,9,15]
sol = Solution2()
print(sol.findUnsortedSubarray(nums))

            


            