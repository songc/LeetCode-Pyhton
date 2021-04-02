# 90. 子集 II
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ansSet = set()
        nums.sort()
        def backtrace(cnt,ind):
            if ind==len(nums):
                return
            for i in range(ind,len(nums)):
                cnt.append(nums[i])
                ansSet.add(tuple(cnt))
                backtrace(cnt,i+1)
                cnt.pop()
        backtrace([],0)
        ans = []
        ans.append([])
        for t in ansSet:
            ans.append(list(t))
        return ans

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ans.append([])
        nums.sort()
        def backtrace(cnt,ind):
            if ind==len(nums):
                return
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                cnt.append(nums[i])
                ans.append(list(cnt))
                backtrace(cnt,i+1)
                cnt.pop()
        backtrace([],0)
        return ans

sol = Solution()

nums = [4,4,4,1,4]

print(sol.subsetsWithDup(nums))