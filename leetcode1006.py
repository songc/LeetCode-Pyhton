# 1006. 笨阶乘
# 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。

# 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。

# 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。

# 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。

# 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/clumsy-factorial
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
class Solution:
    def clumsy(self, N: int) -> int:
        ans=N
        opearte = ["*","/","+","-"]
        deque=collections.deque()
        count = 0
        for i in range(N-1, 0,-1):
            ope = opearte[count%4]
            if ope=="*":
                ans = ans*i
            elif ope=="/":
                ans = ans//i
            elif ope=="+":
                deque.append(ans)
                deque.append(ope)
                deque.append(i)
            elif ope=="-":
                deque.append(ope)
                ans = i
            count+=1
        if deque and deque[-1]=="-":
            deque.append(ans)
        while len(deque)>1:
            num1 = deque.popleft()
            ope = deque.popleft()
            num2 = deque.popleft()
            if ope=="+":
                ans = num1+num2
            elif ope=="-":
                ans = num1-num2
            deque.appendleft(ans)
        return ans

import collections
import math
class Solution:
    def clumsy(self, N: int) -> int:
        deque=collections.deque()
        deque.append(N)
        count = 0
        for i in range(N-1, 0,-1):
            ope = count%4
            if ope==0:
                deque.append(deque.pop()*i)
            elif ope==1:
                deque.append(int(deque.pop()/i))
            elif ope==2:
                deque.append(i)
            elif ope==3:
                deque.append(-i)
            count+=1
        return sum(deque)

sol = Solution()
print(sol.clumsy(10))
        
