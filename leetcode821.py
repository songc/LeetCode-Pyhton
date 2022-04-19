# 821. 字符的最短距离
# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

# 返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

# 两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-distance-to-a-character
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indList = []
        for ind, char in enumerate(s):
            if char == c:
                indList.append(ind)
        ans = []
        pre = curr = 0
        for i in range(len(s)):
            if i>=indList[curr]:
                curr=min(curr+1,len(indList)-1)
                pre=min(pre+1,curr-1)
            ans.append(min(abs(i-indList[pre]),abs(i-indList[curr])))
        return ans

sol = Solution()
s = "loveleetcode"
c = "e"
print(sol.shortestToChar(s,c))

        