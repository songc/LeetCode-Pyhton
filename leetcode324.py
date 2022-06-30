# 324. 摆动排序 II
# 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

# 你可以假设所有输入数组都可以得到满足题目要求的结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/wiggle-sort-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        left, right = (len(tmp)-1)//2, len(nums)-1
        ind = 0
        while ind<len(nums):
            nums[ind]=tmp[left]
            ind+=1
            if ind<len(nums):
                nums[ind]=tmp[right]
            left-=1
            right-=1
            ind+=1
