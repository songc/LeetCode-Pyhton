# 150. 逆波兰表达式求值
# 根据 逆波兰表示法，求表达式的值。

# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

#  

# 说明：

# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        deque = list()
        for s in tokens:
            try:
                x = int(s)
                deque.append(x)
            except:
                num2 = deque.pop()
                num1 = deque.pop()
                if s=="+":
                    res = num1+num2
                elif s=="-":
                    res = num1-num2
                elif s == "*":
                    res = num1*num2
                elif s == "/":
                #    _, res = math.modf(num1/num2)
                   res = int(num1/num2)
                deque.append(res)
        return deque[-1]
sol = Solution()
# tokens = ["2","1","+","3","*"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens=["4","13","5","/","+"]
print(sol.evalRPN(tokens))