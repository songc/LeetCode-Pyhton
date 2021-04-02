# 643. 子数组最大平均数 I
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        tmp = maxSum
        for i in range(k,len(nums)):
            tmp =tmp-nums[i-k]+nums[i]
            maxSum=max(tmp,maxSum)
        return maxSum/k