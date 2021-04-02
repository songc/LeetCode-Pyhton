class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p==".*":
            return True
        pchar=[]
        pL = len(p)
        for ind,val in enumerate(p):
            if val=="*":
                continue
            if ind<pL-1 and p[ind+1]=="*":
                pchar.append(val+"*")
                continue
            pchar.append(val)
        lpr = len(pchar)
        ls = len(s)
        dp=[[False]*(lpr+1) for i in range(ls+1)]
        dp[0][0]=True
        for j in range(1, lpr+1):
            if pchar[j-1].endswith("*"):
                dp[0][j]=dp[0][j-1]
        for i in range(1,ls+1):
            for j in range(1, lpr+1):
                if dp[i-1][j-1]==True and self.match(s[i-1],pchar[j-1]):
                    dp[i][j]=True
                    continue
                if pchar[j-1].endswith("*") and self.match(s[i-1],pchar[j-1]) and dp[i-1][j]==True:
                    dp[i][j] = True
                    continue
                if pchar[j-1].endswith("*") and dp[i][j-1]==True:
                    dp[i][j] = True
                    continue
        return dp[ls][lpr]
        
    def match(self, s:str, p:str)->bool:
        if p.endswith("*"):
            if p[0]==s or p[0]==".":
                return True
        if p==".":
            return True
        return s==p
                            
sol = Solution()
# s = "mississipp"
# p = "mis*is*ip*i"
s = "aaa"
p ="ab*ac*a"
print(sol.isMatch(s,p))               
                    
