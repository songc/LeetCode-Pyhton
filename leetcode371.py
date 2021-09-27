# 371. 两整数之和
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK1 = 4294967296  # 2^32
        MASK2 = 2147483648  # 2^31
        MASK3 = 2147483647  # 2^31-1
        while b != 0:
            carry = ((a&b)<<1)%MASK1
            a = (a^b)%MASK1
            b = carry
        if a & MASK2:
            return ~((a^MASK2)^MASK3)
        else:
            return a

sol = Solution()
print(sol.getSum(2,3))