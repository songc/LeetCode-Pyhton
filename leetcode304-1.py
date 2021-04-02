from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            m, n = 0, 0
        else:
            m, n = len(matrix), len(matrix[0])
        preSum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                preSum[i][j] = preSum[i-1][j]+preSum[i][j-1]+matrix[i-1][j-1]-preSum[i-1][j-1]
        self.preSum = preSum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1]-self.preSum[row2+1][col1]-self.preSum[row1][col2+1]+self.preSum[row1][col1]

matrix = [[]]
obj = NumMatrix(matrix)
p = obj.sumRegion(0,0,0,0)
print(p)

# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# obj = NumMatrix(matrix)
# p1 = obj.sumRegion(1, 2, 2, 4)
# p2 = obj.sumRegion(1, 1, 2, 2)
# p3 = obj.sumRegion(2, 1, 4, 3)

# print(p1,p2,p3)