# 2104. 子数组范围和
# 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。

# 返回 nums 中 所有 子数组范围的 和 。

# 子数组是数组中一个连续 非空 的元素序列。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-subarray-ranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            maxT = nums[i]
            minT = nums[i]
            for j in range(i,n):
                maxT = max(maxT,nums[j])
                minT = min(minT,nums[j])
                ans+=maxT-minT
        return ans

sol = Solution()
nums = [4,-2,-3,4,1]
print(sol.subArrayRanges(nums))
