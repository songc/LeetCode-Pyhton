# 396. 旋转函数
# 给定一个长度为 n 的整数数组 nums 。
# 假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
# 返回 F(0), F(1), ..., F(n-1)中的最大值 。
# 生成的测试用例让答案符合 32 位 整数。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-function
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        preSum = [0]
        ans = 0
        for i,num in enumerate(nums):
            preSum.append(preSum[-1]+num)
            ans+=i*num
        tmp = ans
        n = len(nums)
        for i in range(len(nums),0,-1):
            tmp+=preSum[i-1]-preSum[0]+preSum[n]-preSum[i]
            tmp-=(n-1)*nums[i-1]
            ans = max(tmp,ans)
        return ans


class Solution2:
    def maxRotateFunction(self, nums: List[int]) -> int:
        allSum = sum(nums) 
        ans = 0
        for i,num in enumerate(nums):
            ans+=i*num
        tmp = ans
        n = len(nums)
        for i in range(len(nums)-1,-1,-1):
            tmp=tmp+allSum-nums[i]*n
            ans = max(tmp,ans)
        return ans

sol = Solution2()
nums = [4,3,2,6]
print(sol.maxRotateFunction(nums))
            
