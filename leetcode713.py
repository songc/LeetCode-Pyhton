# 713. 乘积小于 K 的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left=right = 0
        tmp =1
        n = len(nums)
        if k==0:
            return 0
        while right<=n:
            while right<n and tmp*nums[right]<k:
                tmp*=nums[right]
                right+=1
            ans+=right-left
            if left<right:
                tmp//=nums[left]
                left+=1
            else:
                right+=1
                left+=1
        return ans

sol = Solution()
nums = [10,5,2,6]
k = 7
print(sol.numSubarrayProductLessThanK(nums, k))
                