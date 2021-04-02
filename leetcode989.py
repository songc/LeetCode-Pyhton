# 989. 数组形式的整数加法
# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        numA=0
        res=[]
        for a in A:
            numA=numA*10+a
        sumT =numA+K
        if sumT==0:
            return [0] 
        while sumT:
            sumT,mod = divmod(sumT,10)
            res.append(mod)
        res.reverse()
        return res

sol = Solution()
A = [9,9,9,9,9,9,9,9,9,9]
K = 1
print(sol.addToArrayForm(A,K))