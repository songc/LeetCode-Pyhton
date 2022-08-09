# 1413. 逐步求和得到正数的最小值
# 给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。

# 你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。

# 请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        curSum = 0
        for n in nums:
            curSum+=n
            ans = min(ans,curSum)
        if ans<0:
            return -ans+1
        else:
            return 1