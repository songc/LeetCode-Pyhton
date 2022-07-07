# 648. 单词替换
# 在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

# 现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

# 你需要输出替换之后的句子。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/replace-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictTree = self.tree(dictionary)
        words = sentence.split()
        for i in range(len(words)):
            tmp = dictTree
            for char in words[i]:
                if char not in tmp or "end" in tmp:
                    break
                tmp = tmp[char]
            if "end" in tmp:
                words[i]=tmp["end"]
        return " ".join(words)

    
    def tree(self, dictionary: List[str]) -> dict():
        ans = dict()
        for word in dictionary:
            tmp = ans
            for char in word:
                if char not in tmp:
                    tmp[char]=dict()
                tmp=tmp[char]
            tmp['end']=word
        return ans