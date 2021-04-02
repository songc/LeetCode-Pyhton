class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        res, num, sign = 0,0,1
        stack = []
        index = 0
        while index < n:
            if s[index] == "(":
                stack.append(res)
                res = 0
                stack.append(sign)
                sign = 1
            elif s[index] == "+":
                sign = 1
            elif s[index] == "-":
                sign = -1
            elif s[index].isdecimal():
                tmp = int(s[index])
                while index+1 < n and s[index+1].isdecimal():
                    index += 1
                    tmp = tmp*10+int(s[index])
                res+=sign*tmp
            elif s[index] == ")":
                res*=stack.pop()
                res+=stack.pop()
            index+=1
        return res

sol = Solution()
s = "-1-2+3"
print(sol.calculate(s))