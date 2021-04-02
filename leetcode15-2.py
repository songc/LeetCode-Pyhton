class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        n = len(nums)
        res=[]
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while(l<r):
                sumTemp=nums[i]+nums[l]+nums[r]
                if sumTemp>0:
                    r-=1
                elif sumTemp==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l+1]==nums[l]:
                        l+=1
                    while l<r and nums[r-1]==nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif sumTemp<0:
                    l+=1
        return res
        
sol=Solution()
nums=[-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))