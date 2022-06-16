# 532. 数组中的 k-diff 数对
# 给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

# 这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：

# 0 <= i < j < nums.length
# |nums[i] - nums[j]| == k
# 注意，|val| 表示 val 的绝对值。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/k-diff-pairs-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        v=set()
        vset = set()
        for i in nums:
            if i-k in vset:
                v.add((i-k,i))
            if i+k in vset:
                v.add((i,i+k))
            vset.add(i)
        return len(v)

sol = Solution()
nums = [1, 2, 3, 4, 5]
k = 1
print(sol.findPairs(nums,k))