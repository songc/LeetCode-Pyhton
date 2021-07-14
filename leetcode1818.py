# 1818. 绝对差值和
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。

# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。

# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。

# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。

# |x| 定义为：

# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 -x


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-absolute-sum-difference
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9+7
        diff = []
        n = len(nums1)
        maxDiff = 0
        for i in range(len(nums1)):
            tmp = abs(nums1[i]-nums2[i])
            diff.append(tmp)
            maxDiff += tmp
            maxDiff %= mod
        nums1.sort()
        res = maxDiff
        if res ==0:
            return res
        for i in range(len(nums2)):
            ind = bisect.bisect_left(nums1,nums2[i])
            if ind<n:
                tmp = min(abs(nums2[i]-nums1[ind-1]),abs(nums2[i]-nums1[ind]))
            else:
                tmp = abs(nums2[i]-nums1[ind-1])
            res = min(res,maxDiff-diff[i]+tmp)
        return res if res>0 else res+mod

sol = Solution()
nums1 = [1,10,4,4,2,7]
nums2 = [9,3,5,1,7,4]
print(sol.minAbsoluteSumDiff(nums1,nums2))
