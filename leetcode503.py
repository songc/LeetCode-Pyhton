# 503. 下一个更大元素 II
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-greater-element-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections
import bisect
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        deque = collections.deque()
        ans = [None]*len(nums)
        for i in range(len(nums)):
            if len(deque)==0:
                deque.append((nums[i],i))
            else:
                while deque:
                    if deque[0][0]<nums[i]:
                        val,ind = deque.popleft()
                        ans[ind]=nums[i]
                    else:
                        break
                bisect.insort_right(deque,(nums[i],i))
        for i in range(len(nums)):
            while deque:
                if deque[0][0]<nums[i]:
                    val,ind = deque.popleft()
                    ans[ind]=nums[i]
                else:
                    break
        while deque:
            val,ind = deque.popleft()
            ans[ind]=-1
        return ans

sol = Solution()
nums = [1,2,1]
print(sol.nextGreaterElements(nums))
            
