# 629. K个逆序对数组
# 给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

# 逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

# 由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/k-inverse-pairs-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        dp=[1]+[0]*k
        for i in range(1,n+1):
            tmpDp = [0]*(k+1)
            for j in range(k+1):
                if j==0:
                    tmpDp[j]=1
                    continue
                tmp = 0
                if j>=i:
                    tmp = dp[j-i]
                tmpDp[j] = tmpDp[j-1]-tmp+dp[j]
                tmpDp[j]%=mod
            dp = tmpDp
        return dp[-1]

sol = Solution()
n = 3
k = 1
print(sol.kInversePairs(n,k))