# 1218. 最长定差子序列
# 给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

# 子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 1
        aDict = dict()
        for i in arr:
            target = i - difference
            if target in aDict:
                aDict[i]=aDict[target]+1
                res = max(res,aDict[i])
            else:
                aDict[i]=1
        return res

class Solution2:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        for i in arr:
            dp[i]=dp[i-difference]+1
        return max(dp.values())

sol = Solution2()
arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(sol.longestSubsequence(arr,difference))
