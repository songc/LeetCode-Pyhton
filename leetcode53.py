# 53. 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

class Solution:
    def maxSubArray(self, nums: list) -> int:
        sumPre = [0]
        for i in nums:
            sumPre.append(sumPre[-1]+i)
        ans = float("-inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                ans = max([ans,sumPre[j]-sumPre[i]])
        return ans

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))
