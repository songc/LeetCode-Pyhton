# 995. K 连续位的最小翻转次数
# 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。

# 返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
# 模拟翻转，超时
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ans = 0
        left,right = 0,K-1
        n = len(A)
        while right<n:
            if A[left]==0:
                ans += 1
                for i in range(left,right+1):
                    A[i]= A[i]^1
            else:
                right+=1
                left+=1
        if sum(A[-K:])==K:
            return ans
        else:
            return -1

sol = Solution()
A = [0,0,0,1,0,1,1,0]
K = 3
print(sol.minKBitFlips(A,K))
