# 479. 最大回文数乘积
# 给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n==1:
            return 9
        maxNum = 10**n-1
        for i in range(maxNum,0,-1):
            p,tmp = i,i
            while tmp!=0:
                p=p*10+tmp%10
                tmp//=10
            x = maxNum
            while x*x>=p:
                if p%x==0:
                    return p%1337
                x-=1

