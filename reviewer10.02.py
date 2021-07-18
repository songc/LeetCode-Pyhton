# 面试题 10.02. 变位词组
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

# 注意：本题相对原题稍作修改
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s  in  strs:
            tmp = [0]*26
            for char in s:
                tmp[ord(char)-ord("a")]+=1
            key = tuple(tmp)
            res[key].append(s)
        return [res[key] for key in res]

sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))