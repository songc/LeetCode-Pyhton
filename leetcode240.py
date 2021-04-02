# 240. 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import bisect
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            ind = bisect.bisect_right(nums,target)
            if nums[ind-1]==target:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        row,col = m-1,0
        while row>=0 and col<n:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                col+=1
            else:
                row-=1
        return False