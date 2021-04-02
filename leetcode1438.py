# 1438. 绝对差不超过限制的最长连续子数组
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

# 如果不存在满足条件的子数组，则返回 0 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
import bisect
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        left = right = 0
        deque = collections.deque()
        while right<len(nums):
            bisect.insort_right(deque,nums[right])
            while deque[-1]-deque[0]>limit:
                deque.remove(nums[left])
                left+=1
            ans = max(right-left+1,ans)
            right+=1
        return ans

sol = Solution()
nums = [4,2,2,2,4,4,2,2]
limit = 0
print(sol.longestSubarray(nums,limit))