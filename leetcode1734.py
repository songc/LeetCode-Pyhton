# 1734. 解码异或后的排列
# 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

# 它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

# 给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-xored-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        allX = 1
        for i in range(2,n+2):
            allX^=i
        odd = 0
        for i in range(1,n,2):
            odd^=encoded[i]
        ans = [odd^allX]
        for en in encoded:
            ans.append(ans[-1]^en)
        return ans

sol = Solution()
encoded = [6,5,4,6]
print(sol.decode(encoded))
            