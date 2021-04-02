from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in range(len(nums)):
            if nums[i]>0:
                nums[nums[i]-1]=-abs(nums[nums[i]-1])
            else:
                nums[-nums[i]-1]=-abs(nums[-nums[i]-1])
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans
    
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(nums))