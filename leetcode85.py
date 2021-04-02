# 85. 最大矩形
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)<1:
            return 0
        newMatrix = []
        rows,cols = len(matrix),len(matrix[0])
        for i in range(rows):
            tmp =[]
            for j in range(cols):
                if matrix[i][j]=="0":
                    tmp.append(0)
                else:
                    if i ==0:
                        tmp.append(1)
                    else:
                        tmp.append(newMatrix[i-1][j]+1)
            newMatrix.append(tmp)
        ans = 0
        for line in newMatrix:
            ans = max(ans,self.maxRectangle(line))
        return ans
        
    def maxRectangle(self, nums:List[int]) -> int:
        newHeight = [0]+nums+[0]
        deque = []
        deque.append(0)
        ans = 0
        for i in range(1,len(newHeight)):
            while newHeight[i]<newHeight[deque[-1]]:
                height = newHeight[deque.pop()]
                width = i-deque[-1]-1
                ans = max(ans,height*width)
            deque.append(i)
        return ans

sol = Solution()
matrix = [["0","0"]]
print(sol.maximalRectangle(matrix))