class Solution:
    def subsets(self, nums: list) -> list:
        ans =[]
        n = len(nums)
        for i in range(1<<n):
            tmp = []
            for j in range(n):
                if i & 1<<j:
                    tmp.append(nums[j])
            ans.append(tmp)
        return ans
sol = Solution()
nums=[1,2,3]
print(sol.subsets(nums))