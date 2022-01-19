# 219. 存在重复元素 II
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        intSet = set()
        for i in range(n):
            if nums[i] in intSet:
                return True
            intSet.add(nums[i])
            if i>=k:
                intSet.remove(nums[i-k])
        return False