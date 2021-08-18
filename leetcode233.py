# 233. 数字 1 的个数
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

class Solution:
    def countDigitOne(self, n: int) -> int:
        sNum = str(n)
        l = len(sNum)
        if l==1:
            return 0 if n==0 else 1
        dpTmp = [0]
        for i in range(l):
            dpTmp.append(dpTmp[-1]*10+10**i) 
        dp = [0]*(l+1)
        for i in range(1,l+1):            
            if sNum[-i]=="0":
                dp[i]=dp[i-1]
            elif sNum[-i]=="1":
                m=n%(10**(i-1))
                dp[i]=dp[i-1]+m+dpTmp[i-1]+1
            else:
                dp[i]=dp[i-1]+dpTmp[i-1]*int(sNum[-i])+10**(i-1)
            
        return int(dp[-1])


sol = Solution()
print(sol.countDigitOne(13))
            

        