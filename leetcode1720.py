# 1720. 解码异或后的数组
# 未知 整数数组 arr 由 n 个非负整数组成。

# 经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。

# 给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。

# 请解码返回原数组 arr 。可以证明答案存在并且是唯一的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-xored-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[first]
        for e in encoded:
            ans.append(ans[-1]^e)
        return ans

encoded = [6,2,7,3]
first = 4
sol = Solution()
print(sol.decode(encoded,first))