# 224. 基本计算器
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。


class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        operates = []
        n = len(s)
        index = 0
        def compute():
            while operates:
                ope = operates.pop()
                if ope == "(":
                    break
                num2 = nums.pop()
                num1 = nums.pop()
                res = None
                if ope == "+":
                    res = num1+num2
                if ope == "-":
                    res = num1-num2
                nums.append(res)
        while index < n:
            if s[index] == "(":
                operates.append(s[index])
            elif s[index] == "+":
                if operates and (operates[-1]=="+" or operates[-1]=="-"):
                    compute()
                operates.append(s[index])
            elif s[index] == "-":
                if operates and (operates[-1]=="+" or operates[-1]=="-"):
                    compute()
                operates.append(s[index])
            elif s[index].isdecimal():
                tmp = int(s[index])
                while index+1 < n and s[index+1].isdecimal():
                    index += 1
                    tmp = tmp*10+int(s[index])
                nums.append(tmp)
            elif s[index] == ")":
                compute()
            index+=1
        compute()
        return nums[-1]

sol = Solution()
s = "1-2+3"
print(sol.calculate(s))
