# 828. 统计子串中的唯一字符
# 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。

# 例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。

# 本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。输入用例保证返回值为 32 位整数。

# 注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections

## 模拟超时
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        n = len(s)
        maxAlp = set(s)
        for i in range(n):
            tmp=0
            vdict = dict()
            for j in range(i,n):
                if s[j] not in vdict:
                    tmp+=1
                    vdict[s[j]]=1
                else:
                    if vdict[s[j]]==1:
                        tmp-=1
                    vdict[s[j]]+=1
                if tmp==0 and len(vdict)==len(maxAlp):
                    break
                ans+=tmp
        return ans


class Solution2:
    def uniqueLetterString(self, s: str) -> int:
        res=0
        indList = collections.defaultdict(list)
        for ind,c in enumerate(s):
            indList[c].append(ind)
        for arr in indList.values():
            arr = [-1]+arr+[len(s)]
            for i in range(1,len(arr)-1):
                res+=(arr[i]-arr[i-1])*(arr[i+1]-arr[i])
        return res



sol = Solution2()
s = "LEETCODE"
print(sol.uniqueLetterString(s))

                

