# 357. 统计各位数字都不同的数字个数
# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。


# 递归
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 10
        if n==2:
            return 91
        ans = 9
        tmp = 9
        
        for i in range(n-1):
            ans*=tmp
            tmp-=1
        return ans+self.countNumbersWithUniqueDigits(n-1)

class Solution2:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 10
        ans = 10
        cur = 9
        for i in range(n-1):
            cur*=9-i
            ans+=cur
        return ans




sol = Solution2()
print(sol.countNumbersWithUniqueDigits(4))
            