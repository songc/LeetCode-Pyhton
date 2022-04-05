# 762. 二进制表示中质数个计算置位
# 给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。

# 计算置位位数 就是二进制表示中 1 的个数。

# 例如， 21 的二进制表示 10101 有 3 个计算置位。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        vset = set((2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,53,57,59,61))
        ans = 0
        for i in range(left,right+1):
            n = bin(i).count('1')
            if n in vset:
                ans+=1
        return ans

sol = Solution()
left = 6
right = 10
print(sol.countPrimeSetBits(left,right))