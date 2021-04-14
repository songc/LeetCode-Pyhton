# 264. 丑数 II
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。

# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans= 1
        nums= [2,3,5]
        count = 1
        while count<n:
            ans+=1
            tmp = ans
            for i in nums:
                while tmp%i==0:
                    tmp=tmp//i
                if tmp==1:
                    count+=1
                    break 
        return ans

class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        p2=p3=p5=1
        for i in range(2,n+1):
            dp2,dp3,dp5 = dp[p2]*2,dp[p3]*3,dp[p5]*5
            dp[i]=min(dp2,dp3,dp5)
            if dp[i]==dp2:
                p2+=1
            if dp[i]==dp3:
                p3+=1
            if dp[i]==dp5:
                p5+=1
        return dp[-1]

sol = Solution2()
print(sol.nthUglyNumber(10))

