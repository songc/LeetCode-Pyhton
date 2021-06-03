# 525. 连续数组
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        indDict = dict()
        tmp = 0
        res = 0
        indDict[0]=-1
        for i in range(len(nums)):
            if nums[i]==0:
                tmp+=1
            else:
                tmp-=1
            if tmp in indDict:
                res = max(res,i-indDict[tmp])
                continue
            indDict[tmp]=i
        return res

sol = Solution()
nums = [0,1,0]
print(sol.findMaxLength(nums))
