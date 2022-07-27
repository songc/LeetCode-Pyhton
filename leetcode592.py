# 592. 分数加减运算
# 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 

# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。



# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/fraction-addition-and-subtraction
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from curses.ascii import isdigit
from math import gcd
from typing import List


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fraList = self.getFrac(expression)
        a = 0
        b = 1 
        for x,y in fraList:
            a = a*y+x*b
            b = b*y
        t = gcd(a,b)
        return "{}/{}".format(a//t,b//t)
    
    def getFrac(self, expression: str) -> List[tuple]:
        ans = []
        n = len(expression)
        ind=0
        while ind<n:
            flag = 1
            a = 0
            b = 0
            if expression[ind] =='-':
                flag = -1
                ind+=1
            if expression[ind]=='+':
                ind+=1
            while expression[ind].isdigit():
                a = a*10+int(expression[ind])
                ind+=1
            ind+=1
            while ind<n and expression[ind].isdigit():
                b = b*10+int(expression[ind])
                ind+=1
            ans.append((flag*a,b))
        return ans

sol = Solution()
expression = "-5/2+10/3+7/9"
print(sol.fractionAddition(expression))     
