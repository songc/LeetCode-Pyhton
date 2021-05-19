# 1738. 找出第 K 大的异或坐标值
# 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。

# 矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。

# 请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import heapq
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m,n = len(matrix)+1,len(matrix[0])+1
        allnum = []
        newMatrx = [[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                newMatrx[i][j]=newMatrx[i-1][j]^newMatrx[i][j-1]^matrix[i-1][j-1]^newMatrx[i-1][j-1]
                heapq.heappush(allnum,newMatrx[i][j])
                while len(allnum)>k:
                    heapq.heappop(allnum)
        return allnum[0]

sol = Solution()
matrix = [[5,2],[1,6]]
k = 1
print(sol.kthLargestValue(matrix,k))
                