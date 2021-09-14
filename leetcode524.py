# 524. 通过删除字母匹配到字典里最长单词
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
from typing import List
import bisect

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        targetDict = collections.defaultdict(list)
        for i in range(len(s)):
            targetDict[s[i]].append(i)
        res = ""
        dictionary.sort()
        for word in dictionary:
            pre = -1
            if len(word)<=len(res):
                continue
            for i in range(len(word)):
                char = word[i]
                if char not in targetDict:
                    break
                ind = bisect.bisect_right(targetDict[char],pre)
                if ind == len(targetDict[char]):
                    break
                pre = targetDict[char][ind]
                if i==len(word)-1:
                    if len(word)>len(res):
                        res = word
        return res

sol = Solution()
s = "abpcplea"
dictionary = ["a","b","c"]
print(sol.findLongestWord(s,dictionary))
