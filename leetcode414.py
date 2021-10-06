# 414. 第三大的数
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
from typing import List
from sortedcontainers import SortedList


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res = [nums[0]]
        for i in range(1,len(nums)):
            for j in range(len(res)):
                if nums[i]==res[j]:
                    break
                if nums[i]>res[j]:
                    res.insert(j,nums[i])
                    break
            else:
                res.append(nums[i])
            if len(res)>3:
                res.pop()
        return res[-1] if len(res)==3 else res[0]


class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        res = list(set(nums))
        res.sort()
        return res[-3] if len(res)>=3 else res[-1]

class Solution3:
    def thirdMax(self, nums: List[int]) -> int:
        res = SortedList()
        for num in nums:
            if num not in res:
                res.add(num)
                if len(res)>3:
                    res.pop(0)
        return res[0] if len(res)==3 else res[-1]

sol = Solution3()
nums=[1,2,3]
print(sol.thirdMax(nums)) 

    