# 347. 前 K 个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
import collections
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [ i[0] for i in counter.most_common(k)]

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        kv = sorted(((k,counter[k]) for k in counter), key=lambda kv: -kv[1])
        return [kv[i][0] for i in range(k)]

sol = Solution2()
nums = [1,1,1,2,2,3] 
k = 2
print(sol.topKFrequent(nums,k))