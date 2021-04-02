# Error
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
        flag = False
        for sChar in s:
            flag = False
            while(pchar):
                pr = pchar[0]
                if pr.endswith("*"):
                    char= pr[0]
                    if char=="." or char==sChar:
                        flag= True
                        break
                    else:
                        pchar.pop(0)
                        continue
                else:
                    if pr==sChar or pr==".":
                        flag=True
                        pchar.pop(0)
                        break
                    else:
                        return flag
        if flag==True and len(pchar)>0:
            if len(pchar)==1 and pchar[0].endswith("*"):
                return True
            return False
        return flag             

sol = Solution()
s = "mississippi"
p = "mis*is*ip*."
print(sol.isMatch(s,p))