class Solution:
    def threeSum(self, nums: list) -> list:
        n = len(nums)
        numDict = dict()
        for ind, num in enumerate(nums):
            if num not in numDict:
                numDict[num]=[ind]
            else:
                numDict[num].append(ind)
        haset=set()
        res=[]
        for i in range(n):
            for k in range(1,n):
                j = i+k
                if j>=n:
                    break
                target = -(nums[i]+nums[j])
                if frozenset([nums[i],nums[j],target]) in haset:
                    continue  
                if  target in numDict:
                    if set(numDict[target]).difference(set([i,j])):
                        res.append([nums[i],nums[j],target])
                        haset.add(frozenset([nums[i],nums[j],target]))
        return res

sol=Solution()
nums=[-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))