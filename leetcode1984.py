# 1984. 学生分数的最小差值
# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。

# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。

# 返回可能的 最小差值 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        res = nums[-1]
        for i in range(k-1,len(nums)):
            res=min(res,nums[i]-nums[i-k+1])
        return res

sol = Solution()
nums = [9,4,1,7]
k = 2
print(sol.minimumDifference(nums,k))

