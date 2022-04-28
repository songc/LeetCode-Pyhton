# 905. 按奇偶排序数组
# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

# 返回满足此条件的 任一数组 作为答案。

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right = 0, len(nums)-1
        while left<right:
            while left<right and nums[left]%2==0:
                left+=1
            while left<right and nums[right]%2==1:
                right-=1
            nums[left], nums[right] = nums[right], nums[left]
        return nums

sol = Solution()
nums = [3,1,2,4]
print(sol.sortArrayByParity(nums))