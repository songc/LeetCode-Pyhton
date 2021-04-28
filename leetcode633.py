# 633. 平方数之和
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        powSet = set()
        i=0
        while i*i<c:
            n = i*i
            if c-n in powSet:
                return True
            powSet.add(n)
            i+=1
        return False

class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        low,high = 0, int(pow(c,0.5))+1
        while low<=high:
            n=low*low+high*high
            if n==c:
                return True
            elif n<c:
                low+=1
            else:
                high-=1
        return False

sol = Solution2()
c = 10000
print(sol.judgeSquareSum(c))