# 1004. 最大连续1的个数 III
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

# 返回仅包含 1 的最长（连续）子数组的长度。

from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = 0
        left,right = 0,0
        tmp = K
        while right<len(A):
            if A[right]==0:
                tmp -= 1
            while tmp<0:
                if A[left]==0:
                    tmp+=1
                left+=1
            right+=1
            ans = max(ans,right-left)
        return ans

sol = Solution()
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(sol.longestOnes(A,K))
