# 564. 寻找最近的回文数
# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

# “最近的”定义为两个整数差的绝对值最小。


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10**(m-1)-1,10**m+1]
        selfPrefix = int(n[:(m+1)//2])
        for x in range(selfPrefix-1,selfPrefix+2):
            if m%2==0:
                y=x
            else:
                y=x//10
            while y:
                x=x*10+y%10
                y//=10
            candidates.append(x)
        ans = -1
        selfnum = int(n)
        for candidate in candidates:
            if candidate !=selfnum:
                if abs(candidate-selfnum)<abs(ans-selfnum):
                    ans=candidate
        return str(ans)

sol = Solution()
n = "99"
print(sol.nearestPalindromic(n))