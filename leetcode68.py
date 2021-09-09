# 68. 文本左右对齐
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。

# 说明:

# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/text-justification
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        ind = 0
        tmp = []
        tl = 0
        while ind<n:
            while ind<n and tl+len(words[ind])+len(tmp)<=maxWidth:
                tmp.append(words[ind])
                tl+=len(words[ind])
                ind+=1
            if ind==n:
                st = " ".join(tmp)
                st +=" "*(maxWidth-len(st))
                res.append(st)
                continue
            if len(tmp)==1:
                res.append(tmp[0]+" "*(maxWidth-tl))
            elif len(tmp)==2:
                res.append(tmp[0]+" "*(maxWidth-tl)+tmp[1])
            else:
                div,mod = divmod(maxWidth-tl,len(tmp)-1)
                newTmp = [tmp[0]]
                for i in range(1,len(tmp)):
                    t = div
                    if i<=mod:
                        t+=1
                    newTmp.append(" "*t)
                    newTmp.append(tmp[i])
                res.append("".join(newTmp))
            tmp = []
            tl = 0
        return res

sol = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

print(sol.fullJustify(words,maxWidth))
