# 1035. 不相交的线
# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

# 现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：

#  nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

# 以这种方法绘制线条，并返回可以绘制的最大连线数。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/uncrossed-lines
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1),len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1) ]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        return dp[m][n]
sol = Solution()
nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
print(sol.maxUncrossedLines(nums1,nums2))