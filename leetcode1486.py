# 1486. 数组异或操作
# 给你两个整数，n 和 start 。

# 数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

# 请返回 nums 中所有元素按位异或（XOR）后得到的结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xor-operation-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans^=start+2*i
        return ans

sol = Solution()
n = 4
start = 3
print(sol.xorOperation(n,start))