# 930. 和相同的二元子数组
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

# 子数组 是数组的一段连续部分。
from typing import List
import collections


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = [0]
        res = 0
        sumDict = collections.defaultdict(int)
        for num in nums:
            pre.append(pre[-1]+num)
        for p in pre:
            target = p - goal
            if target in sumDict:
                res+=sumDict[target]
            sumDict[p]+=1
        return res


class Solution2:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        sum1 = sum2 =0
        left1 = left2 = right = 0
        n = len(nums)
        while right < n:
            sum1 += nums[right]
            while left1<right and sum1>goal:
                sum1-=nums[left1]
                left1+=1
            sum2 += nums[right]
            while left2<right and sum2>=goal:
                sum2-=nums[left2]
                left2+=1
            res+= left2-left1
            right+=1
        return res
            

sol = Solution2()
nums = [1,0,1,0,1]
goal = 2
print(sol.numSubarraysWithSum(nums,goal))
