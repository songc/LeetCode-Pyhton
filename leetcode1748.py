# 1748. 唯一元素的和

# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

# 请你返回 nums 中唯一元素的 和 。

from typing import List
import collections

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        vdict = collections.defaultdict(int)
        for i in nums:
            vdict[i]+=1
        return sum(i for i in vdict if vdict[i]==1)

sol = Solution()
nums = [1,2,1,2]
print(sol.sumOfUnique(nums))
        