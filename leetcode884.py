# 884. 两句话中的不常见单词
# 句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。

# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。

# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/uncommon-words-from-two-sentences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word1 = collections.defaultdict(int)
        word2 = collections.defaultdict(int)
        for w in s1.split():
            word1[w]+=1
        for w2 in s2.split():
            word2[w2]+=1
        res = []
        for key in word1:
            if word1[key]==1 and key not in word2:
                res.append(key)
        for key in word2:
            if word2[key]==1 and key not in word1:
                res.append(key)
        return res

sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(sol.uncommonFromSentences(s1,s2))
        