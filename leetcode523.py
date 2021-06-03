# 523. 连续的子数组和
# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 如果存在，返回 true ；否则，返回 false 。

# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/continuous-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        preSum = 0
        for n in nums:
            last = preSum
            preSum+=n
            preSum %= k
            if preSum in modes:
                return True
            modes.add(last)
            last = preSum
        return False


class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # 上一个前缀和，下一个就可以用了（距离为2了）
            modes.add(last)
        return False


sol = Solution2()
nums = [23,2,6,4,7]
k=13
print(sol.checkSubarraySum(nums,k))
            
            
