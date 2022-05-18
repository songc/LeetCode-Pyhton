# 668. 乘法表中第k小的数
# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

# 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m*n
        while left<right:
            mid = (left+right)//2
            if self.findXnum(m,n,mid)>=k:
                right = mid
            else:
                left = mid+1
        return left


    def findXnum(self, m, n, target):
        return sum(min(target//i ,n) for i in range(1,m+1))

sol = Solution()
m = 2
n = 3
k = 6
print(sol.findKthNumber(m,n,k))