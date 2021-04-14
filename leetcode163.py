# 263. 丑数
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        nums= [2,3,5]
        for i in nums:
            while n%i==0:
                n=n//i
            if n==1:
                return True
        return False

sol =Solution()
print(sol.isUgly(14))