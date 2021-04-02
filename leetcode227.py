# 227. 基本计算器 II
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

# 整数除法仅保留整数部分。

class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        operates = []
        n = len(s)
        degree = {
            "+": 2,
            "-": 2,
            "*": 3,
            "/": 3,
        }
        index = 0
        def compute():
            if not operates:
                return 
            ope = operates.pop()
            num2 = nums.pop()
            num1 = nums.pop()
            res = None
            if ope == "+":
                res = num1+num2
            elif ope == "-":
                res = num1-num2
            elif ope == "*":
                res = num1*num2
            elif ope == "/":
                res = num1//num2
            nums.append(res)
        while index < n:
            if s[index] == "(":
                operates.append(s[index])
            elif s[index] == ")":
                while operates[-1] != "(":
                    compute()
                operates.pop()
            elif s[index] in degree:
                while operates and (operates[-1] in degree) and degree[operates[-1]] >= degree[s[index]]:
                    compute()
                operates.append(s[index])
            elif s[index].isdecimal():
                tmp = int(s[index])
                while index+1 < n and s[index+1].isdecimal():
                    index += 1
                    tmp = tmp*10+int(s[index])
                nums.append(tmp)
            index+=1
        while operates:
            compute()
        return nums[-1]

sol = Solution()
s = "1+2*5/3+6/4*2"
print(sol.calculate(s))