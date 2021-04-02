# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m,n = len(matrix),len(matrix[0])
        # numCircle = (min(m,n)+1)//2
        # ans = []
        # # if m==1 or n==1:
        # #     for m in matrix:
        # #         ans.extend(m)
        # #     return ans
        # for step in range(numCircle):
        #     for i in range(step,n-step):
        #         ans.append(matrix[step][i])
        #     for i in range(step+1,m-step):
        #         ans.append(matrix[i][n-step-1])
        #     for i in range(n-step-2,step+1,-1):
        #         ans.append(matrix[m-step-1][i])
        #     for i in range(m-step-1,step,-1):
        #         ans.append(matrix[i][step])
        #     # if step==n-step-1 or step==m-step-1:
        #     #     ans.append(matrix[step][step])
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

sol = Solution()
maxtrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(maxtrix))