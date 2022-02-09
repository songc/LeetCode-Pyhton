# 2006. 差的绝对值为 K 的数对数目
# 给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。

# |x| 的值定义为：

# 如果 x >= 0 ，那么值为 x 。
# 如果 x < 0 ，那么值为 -x 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
import collections


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans=0
        vdict = collections.defaultdict(int)
        for n in nums:
            ans+=vdict[n+k]
            ans+=vdict[n-k]
            vdict[n]+=1
        return ans

sol = Solution()
nums = [1,2,2,1]
k = 1
print(sol.countKDifference(nums,k))
