# 461. 汉明距离
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

# 给出两个整数 x 和 y，计算它们之间的汉明距离。


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        target = x^y
        ans = 0
        while target:
            if target&1:
                ans+=1
            target>>=1
        return ans

class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        target = x^y
        ans = 0
        while target:
            ans+=1
            target&=target-1
        return ans

sol = Solution3()
print(sol.hammingDistance(4,4))