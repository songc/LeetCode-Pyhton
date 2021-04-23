# 363. 矩形区域不超过 K 的最大数值和
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
from sortedcollections import SortedList
import bisect
# 超时
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix),len(matrix[0])
        sumPre=[[0]*(n+1) for _ in range(m+1)]
        ans = float('-inf')
        for i in range(m):
            for j in range(n):
                sumPre[i+1][j+1]=matrix[i][j]+sumPre[i][j+1]+sumPre[i+1][j]-sumPre[i][j]
                if sumPre[i+1][j+1]==k:
                    return k
                if ans<sumPre[i+1][j+1]<k:
                    ans = sumPre[i+1][j+1]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    continue
                for x in range(i+1,m+1):
                    for y in range(j+1,n+1):
                        tmp = sumPre[x][y]-sumPre[x][j]-sumPre[i][y]+sumPre[i][j]
                        if tmp == k:
                            return k
                        if ans<tmp<k:
                            ans = tmp
        return ans

class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float('-inf')
        m, n = len(matrix),len(matrix[0])
        for i in range(m):
            total = [0]*n
            for j in range(i,m):
                for x in range(n):
                    total[x]+=matrix[j][x]
                sortSum = SortedList([0])
                s = 0
                for t in total:
                    s+=t
                    ind = sortSum.bisect_left(s-k)
                    if ind<len(sortSum):
                        ans = max(ans,s-sortSum[ind])
                    sortSum.add(s)
        return ans

sol = Solution2()
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(sol.maxSumSubmatrix(matrix,k))

                

        
        