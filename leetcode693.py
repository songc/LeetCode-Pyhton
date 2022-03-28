# 693. 交替位二进制数
# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1
        while n:
            cur = n%2
            if cur==pre:
                return False
            pre = cur
            n//=2
        return True



# 位运算
class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0

sol = Solution()
n = 4
print(sol.hasAlternatingBits(n))