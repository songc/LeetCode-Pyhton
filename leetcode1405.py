# 1405. 最长快乐字符串
# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-happy-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        stack=[]
        if a>0:
            stack.append([-a,'a'])
        if b>0:
            stack.append([-b,'b'])
        if c>0:
            stack.append([-c,'c'])
        heapq.heapify(stack)
        ans = []
        while stack:
            count,ch = heapq.heappop(stack)
            if len(ans)>=2 and ans[-2]==ch and ans[-1]==ch:
                if stack:
                    count2,ch2 = heapq.heappop(stack)
                    ans.append(ch2)
                    count2+=1
                    if count2<0:
                        heapq.heappush(stack,[count2,ch2])
                    heapq.heappush(stack,[count,ch])
            else:
                ans.append(ch)
                count+=1
                if count<0:
                    heapq.heappush(stack,[count,ch])
        return "".join(ans)

sol = Solution()
a = 1
b = 1
c = 7
print(sol.longestDiverseString(a,b,c))


