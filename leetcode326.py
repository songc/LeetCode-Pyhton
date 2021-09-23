# 326. 3的幂
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/power-of-three
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 提示：

# -231 <= n <= 231 - 1
 

# 进阶：

# 你能不使用循环或者递归来完成本题吗？

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        tmp = 1
        while tmp<n:
            tmp*=3
        return tmp==n


# 3**19 = 1162261467
class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

sol = Solution()
print(sol.isPowerOfThree(9))
