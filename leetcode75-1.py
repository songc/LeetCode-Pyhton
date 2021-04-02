class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = 0
        pre1 = 0
        for i in range(len(nums)):
            if nums[i]==0:
                if pre1==pre:
                    nums[pre],nums[i]=nums[i],nums[pre]
                else:
                    nums[pre],nums[i]=nums[i],nums[pre]
                    nums[pre1],nums[i]=nums[i],nums[pre1]
                pre1+=1
                pre+=1
                continue       
            if nums[i]==1:
                if i!=pre1:
                    nums[pre1],nums[i]=nums[i],nums[pre1]
                pre1+=1

        

sol = Solution()
nums=[1,0]
print(sol.sortColors(nums))
print(nums) 