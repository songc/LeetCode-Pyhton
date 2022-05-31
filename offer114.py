# 剑指 Offer II 114. 外星文字典
# 现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

# 给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

# 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

# 字符串 s 字典顺序小于 字符串 t 有两种情况：

# 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
# 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/Jf1JuT
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import collections
from itertools import combinations
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = collections.defaultdict(list)
        degree = dict()
        for c in words[0]:
            degree[c]=0
        for s,t in combinations(words,2):
            for c in t:
                degree.setdefault(c,0)
            for t1,t2 in zip(s,t):
                if t1!=t2:
                    g[t1].append(t2)
                    degree[t2]+=1
                    break
            else:
                if len(s)>len(t):
                    return ""
        ans = []
        deque = collections.deque(i for i in degree if degree[i]==0)
        while deque:
            w = deque.popleft()
            ans.append(w)
            for nw in g[w]:
                degree[nw]-=1
                if degree[nw]==0:
                    deque.append(nw)
        if len(degree) == len(ans):
            return "".join(ans)
        return ""


sol = Solution()
words = ["abc","ab"]
print(sol.alienOrder(words))
