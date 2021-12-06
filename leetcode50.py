# 50. Pow(x, n)
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n==1:
            return x
        if n==-1:
            return 1/x
        tmp = abs(n)
        res = x
        count=1
        while count+count<=tmp:
            res=res*res
            count+=count
        res*=self.myPow(x,tmp-count)
        if n<0:
            return 1/res
        return res

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n==1:
            return x
        if n==-1:
            return 1/x
        tmp = abs(n)
        if tmp%2==1:
            res=x*self.myPow(x*x,tmp//2)
        else:
            res=self.myPow(x*x,tmp//2)
        if n<0:
            return 1/res
        return res

sol = Solution2()
x=2.0
n=-3
print(sol.myPow(x,n))