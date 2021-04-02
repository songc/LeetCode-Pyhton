class Solution:
    def letterCombinations(self, digits: str) -> list:
        if len(digits)==0:
            return []
        res=[]
        digitDict=dict([("2","abc"),("3","def"),("4","ghi"),("5","jkl"),("6","mno"),("7","pqrs"),("8","tuv"),("9","wxyz")])
        def backtrack(ind:int, cp:list):
            if ind== len(digits):
                res.append("".join(cp))
            else:
                for s in digitDict[digits[ind]]:
                    cp.append(s)
                    backtrack(ind+1,cp)
                    cp.pop()
        cp=[]
        backtrack(0, cp)
        return res

sol=Solution()
digits=""
print(sol.letterCombinations(digits))
