# 442. 数组中重复的数据
# 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

# 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            ind = (nums[i]-1)%n
            nums[ind]=nums[ind]+n
        ans = []
        for i in range(n):
            if nums[i]>2*n:
                ans.append(i+1)
        return ans

class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ind = abs(nums[i])-1
            if nums[ind]>0:
                nums[ind]=-nums[ind]
            else:
                ans.append(ind+1)
        return ans

sol = Solution2()
nums = [1]
print(sol.findDuplicates(nums))
