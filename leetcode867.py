# 867. 转置矩阵
# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix), len(matrix[0])
        ans = []
        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(matrix[j][i])
            ans.append(tmp)
        return ans

sol = Solution()
matrix = [[1,2,3],[4,5,6]]
print(sol.transpose(matrix))