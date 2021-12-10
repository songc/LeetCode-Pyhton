# 748. 最短补全词
# 给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出并返回 words 中的 最短补全词 。

# 补全词 是一个包含 licensePlate 中所有的字母的单词。在所有补全词中，最短的那个就是 最短补全词 。

# 在匹配 licensePlate 中的字母时：

# 忽略 licensePlate 中的 数字和空格 。
# 不区分大小写。
# 如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。
# 例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。

# 请你找出并返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 最靠前的 那个。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-completing-word
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        targetC = Counter((i for i in licensePlate.lower() if i.isalpha()))
        res = None
        for w in words:
            tmpC = Counter(w.lower())
            flag = True
            for k in targetC:
                if k not in tmpC or tmpC[k]<targetC[k]:
                    flag=False
                    break
            if flag:
                if not res:
                    res=w
                else:
                    if len(w)<len(res):
                        res=w
        return res

sol = Solution()
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(sol.shortestCompletingWord(licensePlate,words))
