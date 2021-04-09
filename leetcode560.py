# 560. 和为K的子数组
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
from typing import List
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        preSum = [0]
        sumDict = collections.defaultdict(int)
        sumDict[0]+=1
        for i in nums:
            cur = preSum[-1]+i
            preSum.append(cur)
            if cur-k in sumDict:
                ans += sumDict[cur-k]
            sumDict[cur]+=1
        return ans

sol = Solution()
nums = [1,1,1]
k=2
print(sol.subarraySum(nums,k))
        
