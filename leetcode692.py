# 692. 前K个高频单词
# 给一非空的单词列表，返回前 k 个出现次数最多的单词。

# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
import collections
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        allEle = sorted([[-x[1],x[0]]  for x in counter.most_common()])
        return [ x[1] for x in allEle[:k]]
        
sol = Solution()
words=["i", "love", "leetcode", "i", "love", "coding"]
k=3
print(sol.topKFrequent(words,k))