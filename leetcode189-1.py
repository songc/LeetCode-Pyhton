class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return
        l = k%n
        nums.reverse()
        self.reverse(nums,0,l-1)
        self.reverse(nums,l,n-1)
    def reverse(self, nums:list, l:int, r:int):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

sol = Solution()
nums=[1,2,3,4,5,6]
k = 3
sol.rotate(nums,k)
print(nums)