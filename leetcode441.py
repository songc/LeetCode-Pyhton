# 441. 排列硬币
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/arranging-coins
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        diff = 1
        while n>0:
            n-=diff
            diff+=1
            if n>=0:
                res+=1
        return res

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=1:
            return abs(n)
        target = 2*n
        left = 1
        right = n
        while left<=right:
            mid = left+(right-left)//2
            tmp = mid*mid+mid
            if tmp<target:
                left=mid+1
            elif tmp==target:
                return mid
            elif tmp>target:
                right=mid-1
        return left-1
            