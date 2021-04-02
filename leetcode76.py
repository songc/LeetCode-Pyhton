# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-window-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetDict=collections.defaultdict(int)
        for tt in t:
            targetDict[tt]+=1
        numDict = collections.defaultdict(int)
        fbe,fen,minDis = 0,0,float("inf")
        begin,end=0,0
        def issuperset():
            for k in targetDict:
                if numDict[k]<targetDict[k]:
                    return False
            return True
        for i in range(len(s)):
            if s[i] in targetDict:
                numDict[s[i]]+=1
                end+=1
                while issuperset():
                    if end-begin<minDis:
                        fbe,fen=begin,end
                        minDis = fen-fbe
                    if s[begin] in targetDict:
                        numDict[s[begin]]-=1
                    begin+=1
            else:
                end+=1
        return s[fbe:fen]
sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))  



