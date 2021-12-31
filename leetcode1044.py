# 1044. 最长重复子串
# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

# 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-duplicate-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections

# 超时
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        sDict = collections.defaultdict(list)
        n = len(s)
        maxL=0
        res=""
        ind=0
        while ind<n:
            if s[ind] not in sDict:
                sDict[s[ind]].append(ind)
                ind+=1
                continue
            for nInd in sDict[s[ind]]:
                count=0
                while ind+count<n and s[ind+count]==s[nInd+count]:
                    count+=1
                if count and maxL<count:
                    maxL=count
                    res=s[ind:ind+count]
            sDict[s[ind]].append(ind)
            ind+=1
        return res

# 暴力+优化
class Solution2:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        res= ""
        maxLen=0
        i=0
        j=1
        while i<n and j<n:
            if s[i:j] in s[i+1:]:
                if maxLen<j-i:
                    maxLen=j-i
                    res = s[i:j]
            else:
                i+=1
            j+=1
        return res

sol = Solution2()
s = "banana"
print(sol.longestDupSubstring(s))

                

                

