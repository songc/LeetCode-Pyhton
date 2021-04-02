# 55. 跳跃游戏
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标。
class Solution:
    def canJump(self, nums: list) -> bool:
        maxInd = 0
        n = len(nums)
        for ind, num in enumerate(nums):
            if ind>maxInd:
                break
            maxInd = max(ind+num,maxInd)
            if maxInd >= n-1:
                return True
        return False

sol = Solution()
nums=[2,3,1,1,4]
print(sol.canJump(nums))