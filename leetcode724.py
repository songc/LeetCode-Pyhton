# 724. 寻找数组的中心索引
# 给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

# 我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-pivot-index
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def pivotIndex(self, nums: list) -> int:
        preSum=[0]
        for num in nums:
            preSum.append(preSum[-1]+num)
        ans = -1
        midSum = preSum[-1]/2
        for i in range(len(nums)):
            if preSum[i]*2+nums[i]==preSum[-1]:
                ans = i
                break
        return ans
sol = Solution()
nums=[-1,-1,-1,-1,-1,0]
print(sol.pivotIndex(nums))
