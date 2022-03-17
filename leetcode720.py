# 720. 词典中最长的单词

# 给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。

# 若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        wset = set()
        wset.add("")
        ans = ""
        for w in words:
            if w[:-1] in wset:
                wset.add(w)
                if len(w)>len(ans):
                    ans=w
                elif len(w)==len(ans) and w<ans:
                    ans=w
        return ans

sol = Solution()
words = ["w","wo","wor","worl", "world"]
print(sol.longestWord(words))