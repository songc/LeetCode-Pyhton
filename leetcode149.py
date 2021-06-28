# 149. 直线上最多的点数
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
from typing import List
import collections

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        if n<=2:
            return n
        target = n//2+1
        for i in range(n):
            dxDict = collections.defaultdict(int)
            for j in range(n):
                if i ==j:
                    continue
                if points[i][0]-points[j][0]==0:
                    dx = float('inf')
                else:
                    dx = (points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                dxDict[dx]+=1
                res = max(res,dxDict[dx]+1)
            if res > target:
                break
        return res

sol = Solution()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(sol.maxPoints(points))