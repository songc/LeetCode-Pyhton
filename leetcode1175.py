# 1175. 质数排列
# 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

# 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

# 由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/prime-arrangements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



from sqlalchemy import true


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10**9+7
        count = 0 
        for i in range(1,n+1):
            if self.isP(i):
                count+=1
        ans = 1
        for i in range(1,count+1):
            ans*=i
            ans%=mod
        for i in range(1,n-count+1):
            ans*=i
            ans%=mod
        return ans
        
    def isP(self,n:int)->bool:
        if n==1:
            return False
        if n==2:
            return True
        if n==3:
            return True
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

sol = Solution()
print(sol.numPrimeArrangements(5))