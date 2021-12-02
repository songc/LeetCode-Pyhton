# 506. 相对名次
# 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。

# 运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：

# 名次第 1 的运动员获金牌 "Gold Medal" 。
# 名次第 2 的运动员获银牌 "Silver Medal" 。
# 名次第 3 的运动员获铜牌 "Bronze Medal" 。
# 从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
# 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/relative-ranks
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import Counter, List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        vDict = dict()
        for i,v in enumerate(score):
            vDict[v]=i
        sortedScore = sorted(score,reverse=True)
        res = [None]*n
        for i,v in enumerate(sortedScore):
            if i==0:
                res[vDict[v]]="Gold Medal"
                continue
            if i==1:
                res[vDict[v]]="Silver Medal"
                continue
            if i==2:
                res[vDict[v]]="Bronze Medal"
                continue
            res[vDict[v]]=str(i+1)
        return res

sol = Solution()
score = [10,3,8,9,4]
print(sol.findRelativeRanks(score))
