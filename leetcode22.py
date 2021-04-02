# 22. 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

class Solution:
    def generateParenthesis(self, n: int) -> list:
        res=[]
        length = 2*n
        def backtrack(chars:list, left:int, right:int):
            if len(chars)==length:
                res.append("".join(chars))
            if left<n:
                chars.append("(")
                backtrack(chars,left+1,right)
                chars.pop()
            if right<left:
                chars.append(")")
                backtrack(chars, left,right+1)
                chars.pop()
        backtrack([],0,0)
        return res

sol=Solution()
print(sol.generateParenthesis(5))