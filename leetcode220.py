# 220. 存在重复元素 III
# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

# 如果存在则返回 true，不存在返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from sortedcollections import SortedList
import bisect
from typing import List



# 超时
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        for i in range(n):
            for z in range(1, k+1):
                j = i+z
                if j >= n:
                    break
                diff = abs(nums[j]-nums[i])
                if diff <= t:
                    return True
        return False


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sortList = []
        left = right = 0
        while right < len(nums):
            if right-left > k:
                ind = bisect.bisect_left(sortList, nums[left])
                del sortList[ind]
                left += 1
            ind = bisect.bisect_left(sortList, nums[right])
            if sortList and ind < len(sortList) and abs(nums[right]-sortList[ind]) <=t:
                return True
            if sortList and ind>0 and abs(nums[right]-sortList[ind-1])<=t:
                return True
            bisect.insort_right(sortList,nums[right])
            right += 1
        return False

# 桶排序
class Solution3:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        divDict= dict()
        size = t+1
        def getIdx(x):
            if x>=0:
                return x//size
            else:
                return (x+1)//size-1
        left = right = 0
        while right<len(nums):
            if right-left>k:
                divDict.pop(getIdx(nums[left]))
                left+=1
            idx = getIdx(nums[right])
            if idx in divDict:
                return True
            if idx-1 in divDict and abs(divDict[idx-1]-nums[right])<=t:
                return True
            if idx+1 in divDict and abs(divDict[idx+1]-nums[right])<=t:
                return True
            divDict[idx]=nums[right]
            right+=1
        return False
                



sol = Solution3()
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(sol.containsNearbyAlmostDuplicate(nums, k, t))
