# 354. 俄罗斯套娃信封问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

# 说明:
# 不允许旋转信封。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/russian-doll-envelopes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n<=1:
            return n
        sortEnv =  sorted(envelopes)
        dp = [1]*n
        for i in range(n):
            for j in range(i,n):
                if dp[j]<dp[i]+1 and sortEnv[j][0] >sortEnv[i][0] and sortEnv[j][1]>sortEnv[i][1]:
                    dp[j]=dp[i]+1
        return max(dp)

sol = Solution()
envelopes=[[10,8],[1,12],[6,15],[2,18]]
print(sol.maxEnvelopes(envelopes))