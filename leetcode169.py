# 169. 多数元素
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = collections.defaultdict(int)
        ans = None
        for num in nums:
            numsDict[num]+=1
            if not ans or numsDict[num]>numsDict[ans]:
                ans = num
        return ans

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = None
        for num in nums:
            if count==0:
                ans = num
            if num == ans:
                count+=1
            else:
                count-=1
        return ans