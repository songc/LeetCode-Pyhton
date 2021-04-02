# 287. 寻找重复数
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

# 假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-duplicate-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tmp = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in tmp:
                return nums[i]
            else:
                tmp.add(nums[i])

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                return nums[i]

