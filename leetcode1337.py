# 1337. 矩阵中战斗力最弱的 K 行
# 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

# 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。

# 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

# 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            res.append((sum(mat[i]),i))
        res.sort()
        return [t[1] for t in res[:k]]

sol = Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(sol.kWeakestRows(mat,k))