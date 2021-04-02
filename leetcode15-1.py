import bisect
class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        n = len(nums)
        res=[]
        haset=set()
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for k in range(1,n):
                j = i+k
                if j>=n:
                    break
                if k>1 and nums[j]==nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                ind = bisect.bisect_left(nums,target,j+1)
                if ind<n and nums[ind]==target:
                    res.append([nums[i],nums[j],target])
        return res

sol=Solution()
nums=[-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))