# 29. 两数相除
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/divide-two-integers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        t = 2**31-1
        t2= 2**31
        res = 0
        x = abs(dividend)
        y = abs(divisor)
        step = 1
        while x>=y or step>1:
            if x>=y:
                x-=y
                res+=step
                y+=y
                step+=step
            else:
                y = abs(divisor)
                step=1
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            return res if res<=t else t
        else:
            return -res if res<=t2 else -t2


class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        INTMAX, INTMIN= 2**31-1, -2**31 
        if divisor==1:
            return dividend
        if divisor==-1:
            if dividend == INTMIN:
                return INTMAX
            else:
                return -dividend
        res = 0
        x = abs(dividend)
        y = abs(divisor)
        step = 1
        while x>=y or step>1:
            if x>=y:
                x-=y
                res+=step
                y+=y
                step+=step
            else:
                y = abs(divisor)
                step=1
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            return res
        else:
            return -res

sol = Solution2()
dividend = -2147483648
divisor = -1
print(sol.divide(dividend,divisor))
