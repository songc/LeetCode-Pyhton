# 172. 阶乘后的零
# 给定一个整数 n ，返回 n! 结果中尾随零的数量。

# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        for i in range(5,n+1,5):
            while i%5==0:
                i//=5
                ans+=1
        return ans


class Solution2:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n//=5
            ans+=n
        return ans

sol = Solution()
print(sol.trailingZeroes(30))