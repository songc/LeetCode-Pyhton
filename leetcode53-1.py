class Solution:
    def maxSubArray(self, nums: list) -> int:
        dp = []
        for i in range(len(nums)):
            if not dp:
                dp.append(nums[i])
            else:
                tmp = max([dp[-1]+nums[i],nums[i]])
                dp.append(tmp)
        return max(dp)

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))