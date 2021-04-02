# 697. 数组的度
# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/degree-of-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(list)
        for ind,num in enumerate(nums):
            cnt[num].append(ind)
        ans = []
        for key in cnt.keys():
            tmp = [len(cnt[key]),cnt[key][0]-cnt[key][-1]-1]
            ans= max(ans,tmp)
        return -ans[-1]

sol = Solution()
nums=[1,2,2,3,1,4,2]
print(sol.findShortestSubArray(nums))
