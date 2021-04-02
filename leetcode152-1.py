from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        imin = nums[0]
        imax = nums[0]
        ans = imax
        for i in range(1,n):
            tmpMin,tmpMax = imin,imax
            imax = max(nums[i],nums[i]*tmpMax,nums[i]*tmpMin)
            imin = min(nums[i],tmpMin*nums[i],tmpMax*nums[i])
            ans = max(imax,ans)
        return ans