# 397. 整数替换
# 给定一个正整数 n ，你可以做如下操作：

# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# n 变为 1 所需的最小替换次数是多少？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/integer-replacement
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:
            return 0
        if n==2:
            return 1
        if n%2==0:
            return 1+self.integerReplacement(n//2)
        else:
            return 2+min(self.integerReplacement((n+1)//2),self.integerReplacement((n-1)//2))

sol = Solution()
print(sol.integerReplacement(7))