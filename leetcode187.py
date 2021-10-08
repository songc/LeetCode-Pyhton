# 187. 重复的DNA序列
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/repeated-dna-sequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        strSet = set()
        resSet = set()
        for i in range(10,len(s)+1):
            tmp = s[i-10:i]
            if tmp in strSet:
                resSet.add(tmp)
                continue
            strSet.add(tmp)
        return list(resSet)

class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        strDict = collections.defaultdict(int)
        res = []
        for i in range(10,len(s)+1):
            tmp = s[i-10:i]
            strDict[tmp]+=1
            if strDict[tmp]==2:
                res.append(tmp)
        return res

sol = Solution2()
s = "AAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))