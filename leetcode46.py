# 46. 全排列
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

class Solution:
    def permute(self, nums: list) -> list:
        ans=[]
        n = len(nums)
        tmpSet = set()
        def backtrace(oneList,target):
            if len(oneList)==target:
                ans.append(list(oneList))
                return
            for n in nums:
                if n in tmpSet:
                    continue
                oneList.append(n)
                tmpSet.add(n)
                backtrace(oneList,target)
                tmpSet.remove(n)
                oneList.pop()
        backtrace([],n)
        return ans
sol=Solution()
nums=[1,2,3]
print(sol.permute(nums))
