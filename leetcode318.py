# 318. 最大单词长度乘积
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

#  

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        n=len(words)
        newList = []
        for i in words:
            tmp = dict()
            tmp['len']=len(i)
            tmp['cnt']=set(i)
            newList.append(tmp)
        for i in range(n-1):
            for j in range(i+1,n):
                if any( k in newList[j]['cnt'] for k in newList[i]['cnt']):
                    continue
                res = max(newList[i]['len']*newList[j]['len'],res)
        return res

sol = Solution()
words=["abcw","baz","foo","bar","xtfn","abcdef"]
print(sol.maxProduct(words))