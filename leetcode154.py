# 154. 寻找旋转排序数组中的最小值 II
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

# 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        if lo==hi:
            return nums[lo]
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid]==nums[hi]:
                hi-=1
            elif nums[mid]>nums[hi]:
                lo=mid+1
            else:
                hi = mid
        return nums[lo]

sol = Solution()
nums= [0,1]
print(sol.findMin(nums))
                