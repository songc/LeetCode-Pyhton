# 221. 最大正方形
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n =len(matrix),len(matrix[0])
        tmp = [0]*n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    tmp[j]+=1
                else:
                    tmp[j]=0
            ans = max(ans,self.maxSquare(tmp))
        return ans
        

    def maxSquare(self, tmpList):
            deque = [0]
            nums = [0]+list(tmpList)
            nums.append(0)
            ans = 0
            for i in range(len(nums)):
                while nums[i]<nums[deque[-1]]:
                    ind =deque.pop()
                    width = i-deque[-1]-1
                    height = nums[ind]
                    ans =max(ans, min(width,height)**2)
                deque.append(i)
            return ans

sol = Solution()
nums = [3,0,3,2]
print(sol.maxSquare(nums))
matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]

print(sol.maximalSquare(matrix))