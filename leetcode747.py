# 747. 至少是其他数字两倍的最大数
# 给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。

# 请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        a,b=-1,0
        for i in range(1,len(nums)):
            if nums[i]>nums[b]:
                a,b=b,i
            elif a==-1 or nums[a]<nums[i]:
                a=i
        if nums[a]*2<=nums[b]:
            return b
        return -1

sol = Solution()
nums = [3,6,1,0]
print(sol.dominantIndex(nums))