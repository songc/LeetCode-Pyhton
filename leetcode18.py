class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i==0 or nums[i] != nums[i-1]:
                tres=self.threeSum(nums, target-nums[i],i+1)
                for t in tres:
                    res.append([nums[i]]+t)
        return res

    def threeSum(self, nums: list, target:int, lo:int, hi=None) -> list:
        res=[]
        if hi is None:
            hi=len(nums)
        for i in range(lo,hi):
            if i==lo or nums[i]!= nums[i-1]:
                tmp = target-nums[i]
                left = i+1
                right = hi-1
                while(left<right):
                    tsum=nums[left]+nums[right]
                    if tsum<tmp:
                        left+=1
                    elif tsum==tmp:
                        res.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif tsum>tmp:
                        right-=1
        return res

sol=Solution()
nums=[-1, 0, 1, 2, -1, -4]
print(sol.fourSum(nums,target=0))