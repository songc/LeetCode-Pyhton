# 304. 二维区域和检索 - 矩阵不可变
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。


# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        preSum = []
        m = n = len(matrix)
        if m>0:
            n = len(matrix[0])
        for i in range(m):
            tmp = [0]
            for j in range(n):
                tmp.append(tmp[-1]+matrix[i][j])
            preSum.append(tmp)
        self.preSum = preSum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        if len(self.preSum[0])==1:
            return ans
        for row in range(row1,row2+1):
            ans += self.preSum[row][col2+1]-self.preSum[row][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
matrix = [[]]

obj = NumMatrix(matrix)
p = obj.sumRegion(0,0,0,0)
print(p)
# p1 = obj.sumRegion(1, 2, 2, 4)
# p2 = obj.sumRegion(1, 1, 2, 2)
# p3 = obj.sumRegion(2, 1, 4, 3)

# print(p1,p2,p3)