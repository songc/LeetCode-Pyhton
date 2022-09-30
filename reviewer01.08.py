# 面试题 01.08. 零矩阵
# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        rset = set()
        cset = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rset.add(i)
                    cset.add(j)
        for i in range(m):
            for j in range(n):
                if i in rset or j in cset:
                    matrix[i][j]=0