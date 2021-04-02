# 1178. 猜字谜
# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。

# 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：

# 单词 word 中包含谜面 puzzle 的第一个字母。
# 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
# 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
# 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # ans = []
        # wordDict = collections.defaultdict(list)
        # for word in words:
        #     key =frozenset(word)
        #     wordDict[key].append(word)
        # def backtrace(tset, tlist, word, ind):
        #     if ind>=len(word):
        #         return
        #     tset.add(word[ind])
        #     key = frozenset(tset) 
        #     if key in wordDict:
        #         tlist.append(len(wordDict[key]))
        #     backtrace(tset, tlist, word, ind+1)
        #     tset.remove(word[ind])
        #     backtrace(tset, tlist, word, ind+1)
            


        # for puzzle in puzzles:
        #     tmp = []
        #     key = frozenset(puzzle[0])
        #     if key in wordDict:
        #         tmp.append(len(wordDict[key]))
        #     backtrace(set(puzzle[0]), tmp, puzzle, 1)
        #     ans.append(sum(tmp))
        # return ans
        ans = []
        wordDict = collections.defaultdict(int)
        for word in words:
            key =frozenset(word)
            wordDict[key]+=1
        def backtrace(tset, tlist, word, ind):
            if ind>=len(word):
                return
            tset.add(word[ind])
            key = frozenset(tset) 
            if key in wordDict:
                tlist.append(wordDict[key])
            backtrace(tset, tlist, word, ind+1)
            tset.remove(word[ind])
            backtrace(tset, tlist, word, ind+1)
            


        for puzzle in puzzles:
            tmp = []
            key = frozenset(puzzle[0])
            if key in wordDict:
                tmp.append(wordDict[key])
            backtrace(set(puzzle[0]), tmp, puzzle, 1)
            ans.append(sum(tmp))
        return ans

sol = Solution()
words = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
print(sol.findNumOfValidWords(words,puzzles))
