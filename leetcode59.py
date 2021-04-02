# 59. 螺旋矩阵 II
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def getNext(n):
            for i in range(1, n*n+1):
                yield i
        f = getNext(n)
        ans = [[None]*n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                ans[top][i] = next(f)
            for i in range(top+1, bottom+1):
                ans[i][right] = next(f)
            if left < right and top < bottom:
                for i in range(right-1, left, -1):
                    ans[bottom][i] = next(f)
                for i in range(bottom, top, -1):
                    ans[i][left] = next(f)
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans


sol = Solution()
print(sol.generateMatrix(3))
