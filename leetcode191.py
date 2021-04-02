# 191. 位1的个数
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n).count("1")

class Solution2:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n-1
            ans+=1
        return ans

sol = Solution2()
n= 0b00000000000000000000000000001011
print(sol.hammingWeight(n))

