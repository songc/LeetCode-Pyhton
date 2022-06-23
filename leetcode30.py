# 30. 串联所有单词的子串
# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/substring-with-concatenation-of-all-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n, l= len(words),len(words[0]), len(s)
        ans = []
        vdict = collections.defaultdict(int)
        for w in words:
            vdict[w]+=1
        for i in range(l-m*n+1):
            tmp = vdict.copy()
            for j in range(i,i+m*n,n):
                w = s[j:j+n]
                if w in vdict and tmp[w]>0:
                    tmp[w]-=1
                else:
                    break
            else:
                ans.append(i)
        return ans

sol = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(sol.findSubstring(s,words))
