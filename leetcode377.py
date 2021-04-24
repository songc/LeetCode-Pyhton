# 377. 组合总和 Ⅳ
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

# 题目数据保证答案符合 32 位整数范围。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        def backtrace(curr,target):
            nonlocal ans
            if curr==target:
                ans+=1
            if curr>target:
                return
            for i in nums:
                curr+=i
                backtrace(curr,target)
                curr-=i
        backtrace(0,target)
        return ans

class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for num in nums:
                if num<=i:
                    dp[i]+=dp[i-num]
        return dp[-1]
        
sol = Solution2()
nums = [3,2,1]
target = 4
print(sol.combinationSum4(nums,target))