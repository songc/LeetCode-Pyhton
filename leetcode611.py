# 611. 有效三角形的个数
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
from typing import List
import bisect


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                l = abs(nums[j]-nums[i])
                r = nums[j]+nums[i]-1
                lo = bisect.bisect_right(nums,l,j+1)
                hi = bisect.bisect_right(nums,r,j+1)
                res+=hi-lo
        return res

class Solution2:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n-2):
            k = i 
            for j in range(i+1,n-1):
                while k+1<n and nums[k+1]<nums[i]+nums[j]:
                    k=k+1
                res+=max(k-j,0)
        return res

class Solution3:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for k in range(n-1,1,-1):
            i,j=0,k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    res+=j-i
                    j-=1
                else:
                    i+=1
        return res

sol = Solution3()
nums = [2,2,3,4]
print(sol.triangleNumber(nums))
