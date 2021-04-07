# 438. 找到字符串中所有字母异位词
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

# 说明：

# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        m,n = len(s),len(p)
        if m<n:
            return ans
        target = dict(collections.Counter(p))
        tSet = set(target.keys())
        left,right = 0,n-1
        currCounter = collections.defaultdict(int)
        for i in range(right):
            currCounter[s[i]]+=1
        while right<len(s):
            currCounter[s[right]]+=1
            if set(currCounter.keys()) == tSet:
                for key in tSet:
                    if currCounter[key]!=target[key]:
                        break
                else:
                    ans.append(left)
            currCounter[s[left]]-=1
            if currCounter[s[left]]==0:
                del currCounter[s[left]]
            left+=1
            right+=1
        return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        m,n = len(s),len(p)
        if m<n:
            return ans
        target = collections.defaultdict(int)
        for char in p:
            target[char]+=1
        left,right = 0,n-1
        currCounter = collections.defaultdict(int)
        for i in range(right):
            currCounter[s[i]]+=1
        while right<len(s):
            currCounter[s[right]]+=1
            if currCounter==target:
                ans.append(left)
            currCounter[s[left]]-=1
            if currCounter[s[left]]==0:
                del currCounter[s[left]]
            left+=1
            right+=1
        return ans
sol = Solution()
s= "ababababab"
p= "aab"
print(sol.findAnagrams(s,p))
            
                
        