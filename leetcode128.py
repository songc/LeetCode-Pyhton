# 128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#  
# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        ans = 0
        for num in nums:
            if num not in dic:
                left = dic.get(num-1,0)
                right = dic.get(num+1,0)
                tmpLength = left+right+1
                dic[num-left]=tmpLength
                dic[num]=tmpLength
                dic[num+right]=tmpLength
                ans = max(tmpLength,ans)
        return ans

sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))