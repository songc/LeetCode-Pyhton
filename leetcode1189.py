# 1189. “气球” 的最大数量

# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

# 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-balloons
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = collections.Counter(text)
        ans = len(text)
        for s in set("balloon"):
            if s=="l" or s=="o":
                ans=min(ans,counter.get(s,0)//2)
            else:
                ans=min(ans,counter.get(s,0))
        return ans

sol = Solution()
text = "leetcode"
print(sol.maxNumberOfBalloons(text))
