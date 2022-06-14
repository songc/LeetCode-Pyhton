# 498. 对角线遍历
# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        flag = True
        ans = []
        m,n = len(mat),len(mat[0])
        i,j = 0,0
        while len(ans)<m*n:
            ans.append(mat[i][j])
            if flag:
                i-=1
                j+=1
                if i<0 and j>=n:
                    i=1
                    j=n-1
                    flag=False
                elif i<0:
                    i=0
                    flag=False
                elif j>=n:
                    j=n-1
                    i=i+2
                    flag = False
            else:
                i+=1
                j-=1
                if i>=m and j<0:
                    i=m-1
                    j=1
                    flag = True
                elif i>=m:
                    i=m-1
                    j=j+2
                    flag = True
                elif j<0:
                    j=0
                    flag = True
        return ans

sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.findDiagonalOrder(mat))


