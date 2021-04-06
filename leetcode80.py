# 80. 删除有序数组中的重复项 II
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        count = 0
        while cur < len(nums)-2:
            if nums[cur]==nums[cur+1]==nums[cur+2]:
                del nums[cur]
            else:
                cur+=1
        return len(nums)

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        slow = fast =2
        while fast < n:
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow

sol = Solution2()
nums = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums))

