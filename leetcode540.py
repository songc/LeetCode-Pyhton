# 540. 有序数组中的单一元素
# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

# 请你找出并返回只出现一次的那个数。

# 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n= len(nums)-1
        left,right= 0,n
        while left<right:
            mid = (left+right)//2
            if nums[mid]==nums[mid^1]:
                left=mid+1
            else:
                right=mid
        return nums[left]

sol = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(sol.singleNonDuplicate(nums))