# 229. 求众数 II
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.defaultdict(int)
        n = len(nums)
        target = n//3
        res = set()
        for i in nums:
            counter[i]+=1
            if counter[i]>target:
                res.add(i)
                if len(res)==2:
                    return list(res)
        return list(res)

sol = Solution()
nums=[1,1,1,3,3,2,2,2]
print(sol.majorityElement(nums))