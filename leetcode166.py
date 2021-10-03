# 166. 分数到小数
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

# 如果小数部分为循环小数，则将循环的部分括在括号内。

# 如果存在多个答案，只需返回 任意一个 。

# 对于所有给定的输入，保证 答案字符串的长度小于 104 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        if numerator==denominator:
            return "1"
        res = []
        if (numerator<0 and denominator>0) or (numerator>0 and denominator<0):
            res.append("-")
        numerator =abs(numerator)
        denominator=abs(denominator)
        if numerator==denominator:
            res.append("1")
            return "".join(res)
        if numerator<denominator:
            res.append("0.")
            mod = numerator
        else:
            div,mod = divmod(numerator,denominator)
            res.append(str(div))
            if mod:
                res.append(".")
        viDict = dict()
        while mod:
            div,mod = divmod(mod*10,denominator)
            if (div,mod) in viDict:
                res.insert(viDict[(div,mod)],"(")
                res.append(")")
                break
            res.append(str(div))
            viDict[(div,mod)]=len(res)-1
        return "".join((res))

sol =Solution()
numerator = 2
denominator = 1
print(sol.fractionToDecimal(numerator,denominator))
        


        