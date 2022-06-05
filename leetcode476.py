# 476. 数字的补数
# 给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

class Solution:
    def findComplement(self, num: int) -> int:
        ind = 0
        for i in range(31,-1,-1):
            if (num>>i) & 1==1:
                ind = i
                break
        res = 0
        for i in range(ind,-1,-1):
            res*=2
            if (num>>i) & 1!=1:
                res+=1
        return res

sol= Solution()
print(sol.findComplement(5))
