# 472. 连接词
# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。

# 连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/concatenated-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        tree=dict()
        
        def add(word):
            tmp=tree
            for s in word:
                if s not in tmp:
                    tmp[s]=dict()
                tmp=tmp[s]
            tmp['end']=True
        
        def dfs(word,ind):
            if len(word)==0:
                return False
            if ind ==len(word):
                return True
            tmp = tree
            while ind < len(word):
                if word[ind]  not in tmp:
                    return False
                tmp = tmp[word[ind]]
                if 'end' in tmp:
                    if dfs(word,ind+1):
                        return True
                ind+=1
            return False
        words.sort(key=len)
        res = []
        for word in words:
            #由于一个连接词由多个更短的非空单词组成，如果存在一个较长的连接词的组成部分之一是一个较短的连接词，则一定可以将这个较短的连接词换成多个更短的非空单词，因此不需要将连接词加入字典树。
            if dfs(word,0):
                res.append(word)
            else:
                add(word)
        return res

sol = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(sol.findAllConcatenatedWordsInADict(words))       
