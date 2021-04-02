class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return
        l = k%n
        if l <=n/2:
            self.rotateRight(nums,l)
        else:
            self.rotateLeft(nums, n-l)

    def rotateLeft(self, nums:list, k: int):
        n = len(nums)
        while k:
            x=nums.pop(0)
            nums.append(x)
            k-=1

    def rotateRight(self, nums:list, k:int):
        while k:
            x = nums.pop()
            nums.insert(0,x)
            k-=1

sol = Solution()
nums=[]
k = 11
sol.rotate(nums,k)
print(nums)