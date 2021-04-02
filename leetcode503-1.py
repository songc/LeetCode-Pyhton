from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums)
        n = len(nums)
        for j in range(n*2):
            i = j%n
            while stack:
                if nums[stack[-1]]<nums[i]:
                    ans[stack.pop()]=nums[i]
                else:
                    break
            stack.append(i)
        return ans

sol = Solution()
nums = [1,2,1]
print(sol.nextGreaterElements(nums))