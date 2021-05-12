# 1310. 子数组异或查询
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。

# 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。

# 并返回一个包含给定查询 queries 所有结果的数组。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xor-queries-of-a-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        preXOR = [0]
        for i in range(len(arr)):
            preXOR.append(preXOR[-1]^arr[i])
        ans = []
        for L,R in queries:
            ans.append(preXOR[L]^preXOR[R+1])
        return ans

sol = Solution()
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(sol.xorQueries(arr,queries))
        