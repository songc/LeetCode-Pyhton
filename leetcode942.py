# 942. 增减字符串匹配
# 由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:

# 如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I' 
# 如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D' 
# 给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/di-string-match
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        soretInd = collections.deque()
        soretInd.append(0)
        n = len(s)
        ans = [0]*(n+1)
        for ind, char in enumerate(s):
            if char=="I":
                soretInd.append(ind+1)
            else:
                soretInd.appendleft(ind+1)
        for ind,rind in enumerate(soretInd):
            ans[rind]=ind
        return ans

sol = Solution()
s = "DDI"
print(sol.diStringMatch(s))

