import bisect
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        n = len(nums)
        minAbs = float("inf")
        res=sum(nums[:3])
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while(l<r):
                sumTemp=nums[i]+nums[l]+nums[r]
                tmpabs=abs(sumTemp-target)
                if tmpabs<minAbs:
                    minAbs=tmpabs
                    res = sumTemp
                if sumTemp>target:
                    r-=1
                elif sumTemp==target:
                    return res
                elif sumTemp<target:
                    l+=1
        return res

sol=Solution()
nums=[-100,-98,-2,-1]
target=-101
print(sol.threeSumClosest(nums,target))