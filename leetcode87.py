# 87. 扰乱字符串
# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
# 如果字符串的长度为 1 ，算法停止
# 如果字符串的长度 > 1 ，执行下述步骤：
# 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
# 随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
# 在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
# 给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/scramble-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
# 超时 卡在286/288个 例子上
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if len(s1)<=3:
            counter1 = collections.Counter(s1)
            counter2 = collections.Counter(s2)
            return counter1==counter2
        counter1 = collections.Counter()
        counter2 = collections.Counter()
        counter3 = collections.Counter()
        for i in range(len(s1)):
            counter1.update(s1[i])
            counter2.update(s2[i])
            counter3.update(s2[-(i+1)])
            if i==len(s1)-1:
                return False
            if counter1==counter2:
                ans = self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:])
                if ans:
                    return ans
            if counter1==counter3:
                ans = self.isScramble(s1[:i+1],s2[-(i+1):]) and self.isScramble(s1[i+1:],s2[:-(i+1)])
                if ans:
                    return ans
        return False

# 记忆化搜索
from functools import lru_cache
class Solution2:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache()
        def dfs(s1, s2, s1b, s1e, s2b, s2e):
            if s1e-s1b != s2e-s2b:
                return False
            if s1e-s1b+1 <=3:
                counter1 = collections.Counter(s1[s1b:s1e+1])
                counter2 = collections.Counter(s2[s2b:s2e+1])
                return counter1==counter2
            counter1 = collections.Counter()
            counter2 = collections.Counter()
            counter3 = collections.Counter()
            n = s1e-s1b+1
            for i in range(n):
                counter1.update(s1[s1b+i])
                counter2.update(s2[s2b+i])
                counter3.update(s2[s2e-i])
                if i==n-1:
                    return False
                if counter1==counter2:
                    ans = dfs(s1,s2,s1b,s1b+i,s2b,s2b+i) and dfs(s1,s2,s1b+i+1,s1e,s2b+i+1,s2e)
                    if ans:
                        return ans
                if counter1==counter3:
                    ans = dfs(s1,s2,s1b,s1b+i,s2e-i,s2e) and dfs(s1,s2,s1b+i+1,s1e,s2b,s2e-i-1)
                    if ans:
                        return ans
            return False
        return dfs(s1,s2,0,len(s1)-1,0,len(s2)-1)

sol = Solution2()
# s1 = "eebaacbcbcadaaedceaaacadccd"
# s2 = "eadcaacabaddaceacbceaabeccd"
s1 = "abcd"
s2 = "bdac"
print(sol.isScramble(s1,s2))


        