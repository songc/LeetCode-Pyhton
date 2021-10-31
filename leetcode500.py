# 500. 键盘行
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

# 美式键盘 中：

# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/keyboard-row
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alpList=[]
        alpList.append(set("qwertyuiop"))
        alpList.append(set("asdfghjkl"))
        alpList.append(set("zxcvbnm"))
        res = []
        for word in words:
            for alset in alpList:
                if alset.issuperset(set(word.lower())) :
                    res.append(word)
                    break
        return res

class Solution2:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        alNums = [0]*26
        alps = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i, chars in enumerate(alps):
            for char in chars:
                alNums[ord(char)-ord("a")]=i
        for word in words:
            flag = True
            colNum = -1
            for char in word.lower():
                if colNum==-1:
                    colNum=alNums[ord(char)-ord('a')]
                else:
                    if colNum!=alNums[ord(char)-ord('a')]:
                        flag=False
                        break
            if flag:
                res.append(word)
        return res


sol= Solution2()
words = ["Hello","Alaska","Dad","Peace"]
print(sol.findWords(words))