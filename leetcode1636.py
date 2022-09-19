# 1636. 按照频率将数组升序排序
# 给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 

# 请你返回排序后的数组。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sort-array-by-increasing-frequency
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        vcount = sorted((cc,-v) for v,cc in c.items())
        ans = []
        for cc,v in vcount:
            ans.extend([-v]*cc)
        return ans

sol = Solution()
nums = [2,3,1,3,2]
print(sol.frequencySort(nums))