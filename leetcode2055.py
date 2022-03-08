# 2055. 蜡烛之间的盘子
# 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

# 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

# 比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
# 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plates-between-candles
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



from typing import List
import bisect

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        for left,right in queries:
            while left<=right and s[left]!="|":
                left+=1
            while right>=left and s[right]!="|":
                right-=1 
            tmp = 0
            for i in range(left,right):
                if s[i]=="*":
                    tmp+=1
            ans.append(tmp)
        return ans


class Solution2:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ind = []
        preSum = 0
        dp =[]
        n = len(s)
        for i in range(len(s)):
            if s[i]=="|":
                ind.append(i)
                preSum=i-len(ind)-ind[0]
            dp.append(preSum)
        if not ind:
            return [0]*len(queries)
        ans = []
        for left,right in queries:
            newLeft = bisect.bisect_left(ind,left)
            if newLeft==len(ind) or ind[newLeft]>=right:
                ans.append(0)
                continue
            ans.append(dp[right]-dp[ind[newLeft]])
        return ans     


sol = Solution2()
# s = "**|**|***|"
# queries = [[2,5],[5,9]]
s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
print(sol.platesBetweenCandles(s,queries))