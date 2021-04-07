# 416. 分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# 注意:

# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# 时间不可取 n！
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         allSum = sum(nums)
#         div,mod =  divmod(allSum,2)
#         if mod!=0:
#             return False
#         nums.sort(key=lambda x: -x)
#         def dfs(target,begin):
#             if begin>=len(nums):
#                 return False
#             ans=False
#             for ind in range(begin,len(nums)):
#                 newtarget = target-nums[ind]
#                 if newtarget<0:
#                     ans = False
#                 elif newtarget==0:
#                     return True
#                 elif newtarget>0:
#                     ans = dfs(newtarget,ind+1)
#                     if ans:
#                         return ans
#             return ans
#         return dfs(div,0)

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        allSum = sum(nums)
        div,mod =  divmod(allSum,2)
        if mod!=0:
            return False
        imax =  max(nums)
        if imax >div:
            return False
        if imax == div:
            return True
        n = len(nums)
        dp=[[False]*(div+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        dp[0][nums[0]]=True
        for i in range(1,n):
            for j in range(1,div+1):
                if nums[i]==j:
                    dp[i][j]=True
                elif nums[i]<j:
                    if dp[i-1][j] or dp[i-1][j-nums[i]]:
                        dp[i][j]=True
                elif nums[i]>j:
                    if dp[i-1][j]:
                        dp[i][j]=True
            if dp[i][div]:
                return True
        return dp[n-1][div]

sol = Solution2()
nums = [14,9,8,4,3,2]
print(sol.canPartition(nums))

        
        