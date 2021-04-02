# 78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

class Solution:
    def subsets(self, nums: list) -> list:
        ans =[]
        ans.append([])
        def backtrack(cnt, be, end):
            for i in range(be, end):
                cnt.append(nums[i])
                ans.append(list(cnt))
                backtrack(cnt,i+1,end)
                cnt.pop()
        backtrack([],0,len(nums))
        return ans

sol = Solution()
nums=[1]
print(sol.subsets(nums))
