# 474. 一和零
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ones-and-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        Len = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in  range(m + 1)] for _ in range(Len + 1)]
        for k in range(1, Len + 1):
            cnt0 = strs[k-1].count('0')
            cnt1 = strs[k-1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k-1][i][j]             #继承
                    if i - cnt0 >= 0 and j - cnt1 >= 0:     #可更新则更新
                        dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-cnt0][j-cnt1] + 1)
            
        return dp[Len][m][n]

class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = s.count('1')
            for i in range(m, cnt0 - 1, -1):    #0-1背包问题，内循环逆序
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1] + 1)
        return dp[m][n]

# 作者：Hanxin_Hanxin
# 链接：https://leetcode-cn.com/problems/ones-and-zeroes/solution/cpython3-1san-wei-dp-2er-wei-dp-by-hanxi-gwli/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


