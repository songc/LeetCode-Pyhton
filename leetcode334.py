# 334. 递增的三元子序列
# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# 超时
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp=[0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    if dp[i]==2:
                        return True
        return False

class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = float('inf')
        for i in range(1,len(nums)):
            if nums[i]>second:
                return True
            elif nums[i]>first:
                second=nums[i]
            else:
                first = nums[i]
        return False


sol = Solution()
nums = [1,2,3,4,5]
print(sol.increasingTriplet(nums))
