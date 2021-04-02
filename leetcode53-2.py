class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans= nums[0]
        tmp = nums[0]
        for i in range(1,len(nums)):
            if tmp<0:
                tmp=nums[i]
            else:
                tmp=tmp+nums[i]
            ans = max(ans,tmp)
        return ans