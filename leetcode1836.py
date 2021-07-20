# 1838. 最高频元素的频数
# 元素的 频数 是该元素在一个数组中出现的次数。

# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

# 超时
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        keys = sorted((c[0] for c in  counter.items()),reverse=True)
        res = 1
        n = len(keys)
        for i in range(n):
            tmp = counter[keys[i]]
            tmpT = k
            for j in range(i+1,n):
                diff = keys[i]-keys[j]
                div, mod = divmod(tmpT,diff)
                if div==0:
                    break
                tn = min(div,counter[keys[j]])
                tmp+=tn
                tmpT -= tn*diff
            res = max(res,tmp)
        return res

class Solution2:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0 
        total = 0
        res = 1
        for r in range(1,n):
            total += (nums[r]-nums[r-1])*(r-l)
            while total>k:
                total -= (nums[r]-nums[l])
                l+=1
            res = max(res,r-l+1)
        return res

sol = Solution2()
# nums = [1,2,4]
# k = 5
nums = [1,4,8,13]
k = 5
print(sol.maxFrequency(nums,k))