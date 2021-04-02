# 766. 托普利茨矩阵
# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/toeplitz-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

sol = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(sol.isToeplitzMatrix(matrix))