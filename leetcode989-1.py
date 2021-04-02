class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        res=[]
        for a in A[::-1]:
            K,mod = divmod(K+a,10)
            res.append(mod)
        while K:
            K,mod = divmod(K,10)
            res.append(mod)
        res.reverse()
        return res
            

sol = Solution()
A = [9,9,9,9,9,9,9,9,9,9]
K = 1
print(sol.addToArrayForm(A,K))