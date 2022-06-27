# 522. 最长特殊序列 II
# 给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。

# 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。

#  s 的 子序列可以通过删去字符串 s 中的某些字符实现。

# 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-uncommon-subsequence-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        vDict= collections.defaultdict(int)
        vset=set()
        def backtrack(s, strList, target, ind):
            if len(strList) == target:
                vset.add("".join(strList))
                return
            if ind==len(s):
                return
            for i in range(ind,len(s)):
                strList.append(s[i])
                backtrack(s,strList,target,i+1)
                strList.pop()
        for s in strs:
            for i in range(1,len(s)+1):
                strList = []
                backtrack(s,strList,i,0)
            for v in vset:
                vDict[v]+=1
            vset.clear()
        ans=-1
        for v in vDict:
            if vDict[v]==1:
                ans=max(ans,len(v))
        return ans

sol = Solution()
strs = ["aabbcc", "aabbcc","cb"]
print(sol.findLUSlength(strs))
            

            